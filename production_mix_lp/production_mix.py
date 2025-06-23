from typing import Dict, List
import pulp

def solve_production_mix(
    products: List[str],
    profits: Dict[str, float],
    resource_requirements: Dict[str, Dict[str, float]],
    resource_limits: Dict[str, float]
) -> Dict[str, float]:
    """
    Solve the production mix linear programming problem.
    
    Args:
        products: List of product names.
        profits: Dictionary mapping product -> profit per unit.
        resource_requirements: Nested dictionary mapping product -> resource -> amount required per unit.
        resource_limits: Dictionary mapping resource -> total available amount.
        
    Returns:
        Dictionary mapping product -> optimal production quantity.
    """
    # Define the LP problem
    prob = pulp.LpProblem("Production_Mix_Optimization", pulp.LpMaximize)
    
    # Decision variables
    prod_vars = pulp.LpVariable.dicts("ProdQty", products, lowBound=0, cat="Continuous")
    
    # Objective function: maximize total profit
    prob += pulp.lpSum([profits[p] * prod_vars[p] for p in products]), "Total_Profit"
    
    # Constraints: resource limits
    for resource, limit in resource_limits.items():
        prob += (
            pulp.lpSum(resource_requirements[p][resource] * prod_vars[p] for p in products) <= limit,
            f"{resource}_Limit"
        )
    
    # Solve the problem
    prob.solve()
    
    # Extract results
    result = {p: prod_vars[p].varValue for p in products}
    
    return result, prob  # ← Retornamos o modelo para análise adicional


if __name__ == "__main__":
    print("=== Production Mix Optimization ===\n")
    
    # Products and profits
    products = ['Product_A', 'Product_B', 'Product_C']
    profits = {
        'Product_A': 20,
        'Product_B': 30,
        'Product_C': 25
    }

    # Resource usage per product
    resource_requirements = {
        'Product_A': {'Labor_Hours': 2, 'Raw_Material': 3},
        'Product_B': {'Labor_Hours': 4, 'Raw_Material': 2},
        'Product_C': {'Labor_Hours': 3, 'Raw_Material': 5}
    }

    # Total available resources
    resource_limits = {
        'Labor_Hours': 100,
        'Raw_Material': 150
    }

    # Solve and unpack results
    optimal_quantities, model = solve_production_mix(products, profits, resource_requirements, resource_limits)

    # Display optimal production plan
    total_profit = sum(profits[p] * optimal_quantities[p] for p in products)
    print("Optimal production plan:")
    for product, qty in optimal_quantities.items():
        print(f"  {product}: {qty:.2f} units")

    print(f"\nEstimated maximum profit: ${total_profit:.2f}")

    # Display sensitivity analysis
    print("\n--- Sensitivity Analysis ---")
    print(f"{'Resource':<20} {'Shadow Price':>15} {'Slack':>10}")
    print("-" * 50)
    for name, constraint in model.constraints.items():
        shadow_price = constraint.pi
        slack = max(0, round(constraint.slack, 2))  
        print(f"{name:<25} {shadow_price:>15.2f} {slack:>10.2f}")
    
    print("\n==================================")