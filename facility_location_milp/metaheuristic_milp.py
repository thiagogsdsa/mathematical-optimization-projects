import random
import math
from typing import Dict, Tuple
from heuristics_milp import greedy_facility_location  # Make sure this supports 'facilities_open' param
from utils import compute_total_cost  # Your cost function


# def random_neighbor(facilities_open: Dict[str, int]) -> Dict[str, int]:
#     """
#     Flip the open/closed state of one random facility.
#     Ensure at least one facility stays open.
#     """
#     neighbor = facilities_open.copy()
#     keys = list(neighbor.keys())
#     idx = random.randrange(len(keys))
#     key = keys[idx]
#     neighbor[key] = 1 - neighbor[key]

#     if sum(neighbor.values()) == 0:
#         # Force one random facility open if all closed
#         idx2 = random.randrange(len(keys))
#         neighbor[keys[idx2]] = 1

#     return neighbor

def random_neighbor(facilities_open: Dict[str, int], flip_count=2) -> Dict[str, int]:
    neighbor = facilities_open.copy()
    keys = list(neighbor.keys())
    flip_indices = random.sample(range(len(keys)), flip_count)
    for idx in flip_indices:
        key = keys[idx]
        neighbor[key] = 1 - neighbor[key]
    # Ensure at least one open
    if sum(neighbor.values()) == 0:
        neighbor[random.choice(keys)] = 1
    return neighbor


def generate_feasible_initial_solution(
    capacities: Dict[str, float], demands: Dict[str, float]
) -> Dict[str, int]:
    facilities = list(capacities.keys())
    total_demand = sum(demands.values())
    open_facilities = {f: 0 for f in facilities}
    shuffled = random.sample(facilities, len(facilities))
    cap_sum = 0.0
    for f in shuffled:
        open_facilities[f] = 1
        cap_sum += capacities[f]
        if cap_sum >= total_demand:
            break
    return open_facilities

# def simulated_annealing(
#     fixed_costs: Dict[str, float],
#     transport_costs: Dict[str, Dict[str, float]],
#     capacities: Dict[str, float],
#     demands: Dict[str, float],
#     M: float,
#     initial_temperature: float = 5000.0,
#     cooling_rate: float = 0.98,
#     max_iterations: int = 1000,
# ) -> Tuple[Dict[str, int], Dict[str, Dict[str, float]], float]:

#     current_solution = generate_feasible_initial_solution(capacities, demands)
#     open_facilities, current_allocations, _ = greedy_facility_location(
#         fixed_costs, transport_costs, capacities, demands, M, facilities_open=current_solution
#     )
#     current_cost = compute_total_cost(open_facilities, current_allocations, fixed_costs, transport_costs)

#     best_solution = open_facilities.copy()
#     best_allocations = {f: alloc.copy() for f, alloc in current_allocations.items()}
#     best_cost = current_cost

#     temperature = initial_temperature

#     for _ in range(max_iterations):
#         neighbor_solution = random_neighbor(current_solution)
#         open_facilities, neighbor_allocations, _ = greedy_facility_location(
#             fixed_costs, transport_costs, capacities, demands, M, facilities_open=neighbor_solution
#         )
#         allocated = sum(sum(allocs.values()) for allocs in neighbor_allocations.values())
#         total_demand = sum(demands.values())

#         if abs(allocated - total_demand) > 1e-6:
#             neighbor_cost = float("inf")
#         else:
#             neighbor_cost = compute_total_cost(open_facilities, neighbor_allocations, fixed_costs, transport_costs)

#         cost_diff = neighbor_cost - current_cost

#         if cost_diff < 0 or random.random() < math.exp(-cost_diff / temperature):
#             current_solution = neighbor_solution.copy()
#             current_allocations = {f: alloc.copy() for f, alloc in neighbor_allocations.items()}
#             current_cost = neighbor_cost

#             if current_cost < best_cost:
#                 best_solution = current_solution.copy()
#                 best_allocations = {f: alloc.copy() for f, alloc in current_allocations.items()}
#                 best_cost = current_cost

#         temperature *= cooling_rate
#         if temperature < 1e-3:
#             break

#     return best_solution, best_allocations, best_cost

def simulated_annealing(
    fixed_costs: Dict[str, float],
    transport_costs: Dict[str, Dict[str, float]],
    capacities: Dict[str, float],
    demands: Dict[str, float],
    M: float,
    initial_temperature: float = 500.0,
    cooling_rate: float = 0.9,
    max_iterations: int = 500,
) -> Tuple[Dict[str, int], Dict[str, Dict[str, float]], float]:

    total_demand = sum(demands.values())

    current_solution = generate_feasible_initial_solution(capacities, demands)
    open_facilities, current_allocations, _ = greedy_facility_location(
        fixed_costs, transport_costs, capacities, demands, M, facilities_open=current_solution
    )
    allocated = sum(sum(alloc.values()) for alloc in current_allocations.values())

    if abs(allocated - total_demand) > 1e-6:
        current_cost = float("inf")
    else:
        current_cost = compute_total_cost(open_facilities, current_allocations, fixed_costs, transport_costs)

    best_solution = current_solution
    best_allocations = current_allocations
    best_cost = current_cost

    temperature = initial_temperature

    for _ in range(max_iterations):
        neighbor_solution = random_neighbor(current_solution, flip_count=1)

        open_facilities, neighbor_allocations, _ = greedy_facility_location(
            fixed_costs, transport_costs, capacities, demands, M, facilities_open=neighbor_solution
        )

        allocated = sum(sum(alloc.values()) for alloc in neighbor_allocations.values())

        if abs(allocated - total_demand) > 1e-6:
            temperature *= cooling_rate
            continue

        neighbor_cost = compute_total_cost(open_facilities, neighbor_allocations, fixed_costs, transport_costs)
        cost_diff = neighbor_cost - current_cost

        if cost_diff < 0 or random.random() < math.exp(-cost_diff / temperature):
            current_solution = neighbor_solution
            current_allocations = neighbor_allocations
            current_cost = neighbor_cost

            if current_cost < best_cost:
                best_solution = current_solution
                best_allocations = current_allocations
                best_cost = current_cost

        temperature *= cooling_rate
        if temperature < 1e-3:
            break

    return best_solution, best_allocations, best_cost

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

    best_facilities, best_allocations, best_cost = simulated_annealing(
        fixed_costs, transport_costs, capacities, demands, M,
        initial_temperature=1000,
        cooling_rate=0.95,
        max_iterations=1000
    )

    print("Best facilities opened:", best_facilities)
    print("Best allocations:")
    for f, allocs in best_allocations.items():
        print(f"{f}: {allocs}")
    print(f"Best total cost: {best_cost:.2f}")