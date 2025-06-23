import time
import pulp

def solve_facility_location_exact(
    fixed_costs,
    transport_costs,
    capacities,
    demands,
    time_limit=None,
    mip_gap=None,
    threads=1,
    relax_integer=False
):
    """
    Solve Facility Location MILP with performance configs.
    
    Args:
        fixed_costs (dict): facility_id -> fixed opening cost
        transport_costs (dict of dicts): facility_id -> customer_id -> cost
        capacities (dict): facility_id -> capacity
        demands (dict): customer_id -> demand
        time_limit (float or None): max seconds for solver
        mip_gap (float or None): acceptable MIP gap (e.g. 0.01 for 1%)
        threads (int): number of threads to use
        relax_integer (bool): if True, solve LP relaxation (variables continuous)
        
    Returns:
        solution (dict): facility_id -> open(0/1)
                         allocation (dict of dicts): facility_id -> customer_id -> amount
        stats (dict): solver info (time, status, gap, nodes)
    """
    facilities = list(fixed_costs.keys())
    customers = list(demands.keys())
    
    # Define problem
    prob = pulp.LpProblem("Facility_Location", pulp.LpMinimize)
    
    # Variables
    y = {i: pulp.LpVariable(f"y_{i}", cat='Continuous' if relax_integer else 'Binary') for i in facilities}
    x = {(i,j): pulp.LpVariable(f"x_{i}_{j}", lowBound=0, cat='Continuous') for i in facilities for j in customers}
    
    # Objective
    prob += (
        pulp.lpSum(fixed_costs[i]*y[i] for i in facilities)
        + pulp.lpSum(transport_costs[i][j]*x[(i,j)] for i in facilities for j in customers)
    ), "TotalCost"
    
    # Constraints
    # Demand satisfaction
    for j in customers:
        prob += pulp.lpSum(x[(i,j)] for i in facilities) == demands[j], f"Demand_{j}"
    # Capacity constraints
    for i in facilities:
        prob += pulp.lpSum(x[(i,j)] for j in customers) <= capacities[i]*y[i], f"Capacity_{i}"
    
    # Setup solver and parameters
    solver = pulp.PULP_CBC_CMD(msg=True, timeLimit=time_limit, mip=True, gapRel=mip_gap, threads=threads)
    
    # Solve
    start = time.perf_counter()
    prob.solve(solver)
    elapsed = time.perf_counter() - start
    
    # Extract solution
    solution_y = {i: y[i].varValue for i in facilities}
    allocation = {
        i: {j: x[(i,j)].varValue for j in customers}
        for i in facilities
    }
    
    # Stats
    status = pulp.LpStatus[prob.status]
    gap = solver.actualGap if hasattr(solver, "actualGap") else None
    # Nodes info not exposed by CBC wrapper, would need direct API
    
    stats = {
        "status": status,
        "time": elapsed,
        "gap": gap,
    }
    
    return {"open_facilities": solution_y, "allocation": allocation}, stats


if __name__ == "__main__":
    # Example instance
    fixed_costs = {"F1": 1000, "F2": 1200, "F3": 800}
    transport_costs = {
        "F1": {"C1": 10, "C2": 12, "C3": 20},
        "F2": {"C1": 15, "C2": 8, "C3": 25},
        "F3": {"C1": 9, "C2": 14, "C3": 18},
    }
    capacities = {"F1": 100, "F2": 80, "F3": 120}
    demands = {"C1": 70, "C2": 60, "C3": 50}
    
    solution, stats = solve_facility_location_exact(
        fixed_costs, transport_costs, capacities, demands,
        time_limit=30,
        mip_gap=0.01,
        threads=4,
        relax_integer=False
    )
    
    print(f"Solver status: {stats['status']}")
    print(f"Time elapsed: {stats['time']:.2f} seconds")
    print(f"MIP Gap: {stats['gap']}")
    print("\nFacilities opened:")
    for f, val in solution["open_facilities"].items():
        print(f"  {f}: {val:.2f}")
    print("\nAllocations:")
    for f, allocs in solution["allocation"].items():
        for c, amt in allocs.items():
            print(f"  Facility {f} -> Customer {c}: {amt:.2f}")
