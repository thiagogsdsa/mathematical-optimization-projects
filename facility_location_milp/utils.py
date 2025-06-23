from typing import Dict, Tuple

# def compute_total_cost(
#     open_facilities: Dict[str, int],
#     allocations: Dict[str, Dict[str, float]],
#     fixed_costs: Dict[str, float],
#     transport_costs: Dict[str, Dict[str, float]]
# ) -> float:
#     total = 0.0
#     for f, open_flag in open_facilities.items():
#         if open_flag == 1:
#             total += fixed_costs[f]
#             for c, amount in allocations[f].items():
#                 total += amount * transport_costs[f][c]
#     return total

def compute_total_cost(
    open_facilities: Dict[str, int],
    allocations: Dict[str, Dict[str, float]],
    fixed_costs: Dict[str, float],
    transport_costs: Dict[str, Dict[str, float]]
) -> float:
    total = 0.0
    for facility, is_open in open_facilities.items():
        if is_open == 1:
            total += fixed_costs.get(facility, 0)
            allocation = allocations.get(facility, {})
            transport = transport_costs.get(facility, {})
            for customer, amount in allocation.items():
                cost_per_unit = transport.get(customer, 0)
                total += amount * cost_per_unit
    return total

def print_solution(name, open_facilities, allocations, cost, elapsed, verbose=True):
    print(f"--- {name} ---")
    print(f"Total cost: {cost:.2f}")
    print(f"Time elapsed: {elapsed:.4f} seconds")
    if verbose:
        print(f"Facilities opened: {open_facilities}")
        print("Allocations:")
        for f, allocs in allocations.items():
            print(f"  {f}: {allocs}")
    print()  # blank line