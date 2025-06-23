import sys
import os
sys.path.append(os.path.dirname(__file__))
import time
from exact_solver_milp import solve_facility_location_exact
from heuristics_milp import greedy_facility_location
from metaheuristic_milp import simulated_annealing
from utils import compute_total_cost, print_solution
from test_instances import small_instance, medium_instance, large_instance, generate_instance

def main(verbose=True):
    # Select instance
    instance = generate_instance(100,800)  # or small_instance(), medium_instance()

    # Unpack input data
    fixed_costs = instance["fixed_costs"]
    transport_costs = instance["transport_costs"]
    capacities = instance["capacities"]
    demands = instance["demands"]
    M = instance["M"]

    # --- Exact Solver ---
    start = time.time()
    exact_result, _ = solve_facility_location_exact(
        fixed_costs, transport_costs, capacities, demands
    )
    exact_open = exact_result["open_facilities"]
    exact_alloc = exact_result["allocation"]
    exact_cost = compute_total_cost(
        exact_open, exact_alloc, fixed_costs, transport_costs
    )
    exact_time = time.time() - start
    print_solution("Exact MILP", exact_open, exact_alloc, exact_cost, exact_time, verbose)

    # --- Greedy Heuristic ---
    start = time.time()
    heuristic_open, heuristic_alloc, heuristic_cost = greedy_facility_location(
        fixed_costs, transport_costs, capacities, demands, M
    )
    heuristic_time = time.time() - start
    print_solution("Greedy Heuristic", heuristic_open, heuristic_alloc, heuristic_cost, heuristic_time, verbose)

    # --- Metaheuristic (Simulated Annealing) ---
    start = time.time()
    meta_open, meta_alloc, meta_cost = simulated_annealing(
        fixed_costs, transport_costs, capacities, demands, M
    )
    meta_time = time.time() - start
    print_solution("Simulated Annealing", meta_open, meta_alloc, meta_cost, meta_time, verbose)


if __name__ == "__main__":
    # To show detailed output, set verbose=True; to show only cost/time, use verbose=False
    main(verbose=False)
