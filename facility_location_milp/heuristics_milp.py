from typing import Dict, Tuple, Optional
from utils import compute_total_cost

# def greedy_facility_location(
#     fixed_costs: Dict[str, float],
#     transport_costs: Dict[str, Dict[str, float]],
#     capacities: Dict[str, float],
#     demands: Dict[str, float],
#     M: float,  # not used here, but for interface compatibility
#     facilities_open: Dict[str, int] = None  # NEW optional argument
# ) -> Tuple[Dict[str, int], Dict[str, Dict[str, float]], float]:
    
#     # If open facilities are passed in, use them; else initialize as empty and open during allocation
#     if facilities_open is None:
#         open_facilities = {f: 0 for f in fixed_costs}
#     else:
#         open_facilities = facilities_open.copy()

#     allocations = {f: {c: 0.0 for c in demands} for f in fixed_costs}
#     remaining_capacity = capacities.copy()
#     remaining_demand = demands.copy()

#     # For each customer
#     for c in demands:
#         demand_to_assign = remaining_demand[c]
#         # Facilities sorted by cost for this customer, but only consider open ones if facilities_open is given
#         if facilities_open is not None:
#             sorted_facilities = [f for f in fixed_costs if open_facilities[f] == 1]
#             # Sort these open facilities by cost for customer c
#             sorted_facilities.sort(key=lambda f: transport_costs[f][c])
#         else:
#             # If no fixed open, consider all facilities sorted by cost
#             sorted_facilities = sorted(fixed_costs.keys(), key=lambda f: transport_costs[f][c])

#         for f in sorted_facilities:
#             if demand_to_assign <= 0:
#                 break
#             available = remaining_capacity[f]
#             if available <= 0:
#                 continue

#             allocation = min(available, demand_to_assign)
#             allocations[f][c] = allocation
#             remaining_capacity[f] -= allocation
#             demand_to_assign -= allocation

#             if facilities_open is None and allocation > 0:
#                 open_facilities[f] = 1  # open this facility since we allocated here

#     total_cost = compute_total_cost(open_facilities, allocations, fixed_costs, transport_costs)
#     return open_facilities, allocations, total_cost

def greedy_facility_location(
    fixed_costs: Dict[str, float],
    transport_costs: Dict[str, Dict[str, float]],
    capacities: Dict[str, float],
    demands: Dict[str, float],
    M: float,
    facilities_open: Dict[str, int] = None
) -> Tuple[Dict[str, int], Dict[str, Dict[str, float]], float]:
    
    if facilities_open is None:
        facilities_open = {f: 1 for f in fixed_costs}

    open_facilities = {f: 0 for f in fixed_costs}
    allocations = {f: {c: 0.0 for c in demands} for f in fixed_costs}
    remaining_capacity = capacities.copy()

    for c in demands:
        demand_to_assign = demands[c]

        sorted_facilities = sorted(fixed_costs.keys(), key=lambda f: transport_costs[f][c])

        for f in sorted_facilities:
            if facilities_open[f] == 0:
                continue
            if demand_to_assign <= 0:
                break

            available = remaining_capacity[f]
            if available <= 0:
                continue

            allocation = min(available, demand_to_assign)
            allocations[f][c] = allocation
            remaining_capacity[f] -= allocation
            demand_to_assign -= allocation

            if allocation > 0:
                open_facilities[f] = 1

    total_demand = sum(demands.values())
    total_allocated = sum(sum(alloc.values()) for alloc in allocations.values())

    if abs(total_demand - total_allocated) > 1e-6:
        return open_facilities, allocations, float("inf")

    total_cost = compute_total_cost(open_facilities, allocations, fixed_costs, transport_costs)
    return open_facilities, allocations, total_cost

if __name__ == "__main__":
    fixed_costs = {"F1": 1000, "F2": 1200, "F3": 800}
    transport_costs = {
        "F1": {"C1": 10, "C2": 12, "C3": 20},
        "F2": {"C1": 15, "C2": 8, "C3": 25},
        "F3": {"C1": 9, "C2": 14, "C3": 18},
    }
    capacities = {"F1": 100, "F2": 80, "F3": 120}
    demands = {"C1": 70, "C2": 60, "C3": 50}
    M = 1e6

    open_facilities, allocations, cost = greedy_facility_location(
        fixed_costs, transport_costs, capacities, demands, M
    )
    
    print("Facilities opened:", open_facilities)
    print("Allocations:")
    for f, allocs in allocations.items():
        print(f"{f}: {allocs}")
    print(f"Total cost: {cost:.2f}")