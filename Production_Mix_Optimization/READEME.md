# Production Mix Optimization

## Overview

This project demonstrates solving a classic linear programming problem: optimizing the production mix in a factory with limited resources. The goal is to maximize total profit by deciding how many units of each product to produce without exceeding resource constraints.

---

## Problem Description

You manage a factory producing multiple products. Each product consumes limited resources (e.g., labor hours, raw materials) and generates profit per unit. The problem is to determine the optimal production quantities that maximize profit while respecting resource availability.

---

## Mathematical Model

Maximize

$$
Z = \mathbf{p}^\top \mathbf{x} = \sum_{i=1}^n p_i x_i
$$

subject to

$$
A\mathbf{x} \leq \mathbf{b}
$$

and

$$
\mathbf{x} \geq 0
$$

Where:

- $\mathbf{x} := [x_1, x_2, \ldots, x_n]^\top$ is the vector of production quantities
- $\mathbf{p} := [p_1, p_2, \ldots, p_n]^\top$ is the profit per unit vector
- $ A := [r_{ij}]$ is the $m \times n$ resource consumption matrix
- $\mathbf{b} := [b_1, b_2, \ldots, b_m]^\top$ is the resource availability vector
- $n$ is the number of products
- $m$ is the number of resource types

---

### Theoretical Background

This is a classical **Linear Programming (LP)** problem. The feasible region defined by the constraints $A\mathbf{x} \leq \mathbf{b}$ and $\mathbf{x} \geq 0$ forms a **convex polyhedron** in $\mathbb{R}^n$.

According to the **Fundamental Theorem of Linear Programming**:

- If the feasible region is **non-empty**, and the objective function is **bounded above** (in the case of maximization), then an **optimal solution exists**.
- Furthermore, the optimal solution is attained at one of the **vertices (extreme points)** of the feasible region.

This property allows LP problems to be efficiently solved using methods like the **Simplex Algorithm** or **Interior Point Methods**.

---

## Example Input

```python
products = ['Product_A', 'Product_B', 'Product_C']

profits = {
    'Product_A': 20,
    'Product_B': 30,
    'Product_C': 25
}

resource_requirements = {
    'Product_A': {'Labor_Hours': 2, 'Raw_Material': 3},
    'Product_B': {'Labor_Hours': 4, 'Raw_Material': 2},
    'Product_C': {'Labor_Hours': 3, 'Raw_Material': 5}
}

resource_limits = {
    'Labor_Hours': 100,
    'Raw_Material': 150
}

## Running the Optimization

Run the Python script:

```bash
python production_mix.py
```

**Expected Output:**

```yaml
Optimal production plan:
  Product_A: 50.00 units
  Product_B: 0.00 units
  Product_C: 0.00 units

Estimated maximum profit: $1000.00

--- Sensitivity Analysis ---
Resource                Shadow Price      Slack
--------------------------------------------------
Labor_Hours_Limit            6.25             0.00
Raw_Material_Limit           2.50             0.00
```

---

## Interpretation of Results

- **Optimal Plan**: Produce 50 units of Product_A, and none of the others to maximize profit.
- **Profit**: Maximum achievable profit is **$1000.00**.
- **Shadow Price**: Indicates how much the total profit would increase if each resource increased by one unit.
  - Labor_Hours: +$6.25 per extra hour
  - Raw_Material: +$2.50 per extra unit
- **Slack**: Zero means the resource is fully utilized and currently constraining the optimal solution.

---

## File Structure

```
production_mix_optimization/
├── production_mix.py        # Main solver script
├── test_production_mix.py   # Unit tests
├── requirements.txt         # Project dependencies
└── README.md                # Documentation
```

---

## Dependencies

- Python 3.7+
- PuLP
- NumPy (optional)
- Matplotlib (optional)

Install them with:

```bash
pip install -r requirements.txt
```

---

## Unit Testing

Run tests with:

```bash
python -m unittest discover
```

---

## License

MIT License © Thiago Guimarães

---

## Contributions

Contributions, improvements, and questions are welcome!

---

## Contact

Thiago Guimarães
[thiago.guimaraes.sto@gmail.com](mailto:thiago.guimaraes.sto@gmail.com)
[LinkedIn](https://www.linkedin.com/in/thiagogsdsa)
[GitHub](https://github.com/thiagogsdsa)

Project Link: https://github.com/thiagogsdsa/production_mix_optimization
