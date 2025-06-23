"""
Benchmark problem instances for Facility Location Problem.
Each instance is a dictionary with:
- fixed_costs: Dict[str, float]
- transport_costs: Dict[str, Dict[str, float]]
- capacities: Dict[str, float]
- demands: Dict[str, float]
"""

import random


def generate_instance(n_facilities: int, n_customers: int, seed: int = 42) -> dict:
    
    random.seed(seed)

    facilities = [f"F{i+1}" for i in range(n_facilities)]
    customers = [f"C{j+1}" for j in range(n_customers)]

    # Generate customer demands
    demands = {c: random.randint(40, 100) for c in customers}
    total_demand = sum(demands.values())

    # Assign capacities roughly proportional to total demand, with small variation
    base_capacity = total_demand / n_facilities
    capacities = {
        f: int(base_capacity + random.randint(-10, 30))
        for f in facilities
    }

    # Adjust last facility capacity if total capacity is less than total demand
    total_capacity = sum(capacities.values())
    if total_capacity < total_demand:
        last_fac = facilities[-1]
        capacities[last_fac] += int(total_demand - total_capacity) + 10

    # Fixed costs and transportation costs
    fixed_costs = {f: random.randint(500, 2000) for f in facilities}
    transport_costs = {
        f: {c: random.randint(5, 30) for c in customers}
        for f in facilities
    }

    return {
        "fixed_costs": fixed_costs,
        "transport_costs": transport_costs,
        "capacities": capacities,
        "demands": demands,
        "M": 1e6,
    }

# === Predefined instances ===

def small_instance():
    return {
        "fixed_costs": {"F1": 1000, "F2": 1200, "F3": 800},
        "transport_costs": {
            "F1": {"C1": 10, "C2": 12, "C3": 20},
            "F2": {"C1": 15, "C2": 8, "C3": 25},
            "F3": {"C1": 9, "C2": 14, "C3": 18},
        },
        "capacities": {"F1": 100, "F2": 80, "F3": 120},
        "demands": {"C1": 70, "C2": 60, "C3": 50},
        "M": 1e6
    }


def medium_instance():
    return generate_instance(10, 30, seed=123)


def large_instance():
    return generate_instance(300, 500, seed=456)


if __name__ == "__main__":
    print(" Small instance:")
    print(small_instance())
    print("\n Medium instance (summary):")
    mid = medium_instance()
    print(f"{len(mid['fixed_costs'])} facilities, {len(mid['demands'])} customers")

    print("\n Large instance (summary):")
    large = large_instance()
    print(f"{len(large['fixed_costs'])} facilities, {len(large['demands'])} customers")
