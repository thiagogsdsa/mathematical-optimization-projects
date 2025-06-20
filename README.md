# Mathematical Optimization Projects

This repository organizes a series of mathematical optimization projects, arranged by increasing problem complexity. The goal is to showcase practical implementations of various optimization techniques using Python and state-of-the-art solvers.

---

## Project Roadmap

| Level | Project                            | Description                                                                                     | Status         |
|-------|------------------------------------|-------------------------------------------------------------------------------------------------|----------------|
| 1     | Linear Programming (LP)            | Production mix optimization with continuous decision variables and resource constraints.        | ✅ Completed   |
| 2     | Facility Location (MILP)           | Classic mixed-integer model for choosing optimal facility placement based on fixed costs.       | 🚧 In Progress |
| 3     | Knapsack Problem (IP)              | 0-1 knapsack variants modeling binary decisions under capacity constraints.                     | 🗓️ Planned     |
| 4     | Workforce Scheduling (IP / MILP)   | Scheduling shifts with integer constraints and fairness criteria.                               | 🗓️ Planned     |
| 5     | Portfolio Optimization (NLP)       | Optimize asset allocation with nonlinear constraints (e.g., risk measures).                     | 🗓️ Planned     |
| 6     | Multi-Objective Optimization       | Solve conflicting-goal problems using Pareto optimality and scalarization.                      | 🗓️ Planned     |

---
> Note: In this repository, NLP refers to Nonlinear Programming, not Natural Language Processing — though I work on both! 😄

## Projects

### 1. Linear Programming (LP)

- **Folder:** `Production_Mix_Optimization`  
- **Description:** Production mix optimization maximizing profit with linear constraints.  
- **Key Tools:** PuLP, CBC Solver  
- **Status:** ✅ Completed  
- **Link:** [Production_Mix_Optimization](https://github.com/thiagogsdsa/mathematical-optimization-projects/tree/main/Production_Mix_Optimization)

---

### 2. Facility Location (MILP)

- **Folder:** `facility_location_milp`  
- **Description:** Classic MILP formulation to select which facilities to open and assign demand while minimizing total cost (fixed + transportation).  
- **Key Tools:** PuLP, Gurobi/CPLEX (optional), networkx (for graphs)  
- **Status:** 🚧 In Progress  
- **Link:** [facility_location_milp](./facility_location_milp)

---

### 3. Knapsack Problem (IP)

- **Folder:** `knapsack_variants`  
- **Description:** Pure integer program modeling constrained selection problems. Includes classic 0-1 knapsack and bounded knapsack.  
- **Key Tools:** PuLP, CBC Solver  
- **Status:** 🗓️ Planned  
- **Link:** [knapsack_variants](./knapsack_variants)

---

### 4. Workforce Scheduling (IP/MILP)

- **Folder:** `shift_scheduling`  
- **Description:** Solve a shift allocation problem where employees are scheduled under constraints like availability and shift coverage.  
- **Key Tools:** PuLP, Pandas  
- **Status:** 🗓️ Planned  
- **Link:** [shift_scheduling](./shift_scheduling)

---

### 5. Portfolio Optimization (NLP)

- **Folder:** `portfolio_optimization_nlp`  
- **Description:** Mean-variance optimization problem using nonlinear solvers to maximize return while controlling for risk.  
- **Key Tools:** SciPy.optimize, NumPy  
- **Status:** 🗓️ Planned  
- **Link:** [portfolio_optimization_nlp](./portfolio_optimization_nlp)

---

### 6. Multi-Objective Optimization

- **Folder:** `multi_objective_optimization`  
- **Description:** Applies multi-objective optimization with conflicting goals using scalarization and Pareto front techniques.  
- **Key Tools:** DEAP (for genetic algorithms), matplotlib, NumPy  
- **Status:** 🗓️ Planned  
- **Link:** [multi_objective_optimization](./multi_objective_optimization)

---

## Requirements

Each project includes its own `requirements.txt` file, but general dependencies include:

- Python 3.7+
- PuLP
- NumPy
- Matplotlib

Install dependencies with:

```
pip install -r requirements.txt
```

---

## License

MIT License © Thiago Guimarães

---

## Contact

Feel free to reach out:

- **Email:** thiago.guimaraes.sto@gmail.com  
- **LinkedIn:** [linkedin.com/in/thiagogsdsa](https://www.linkedin.com/in/thiagogsdsa)  
- **GitHub:** [github.com/thiagogsdsa](https://github.com/thiagogsdsa)

  
