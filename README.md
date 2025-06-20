# Mathematical Optimization Projects

This repository organizes a series of mathematical optimization projects, arranged by increasing problem complexity. The goal is to showcase practical implementations of various optimization techniques using Python and state-of-the-art solvers.

---

## Project Roadmap

| Level | Project                              | Description                                                                                     | Status    |
|-------|------------------------------------|-------------------------------------------------------------------------------------------------|-----------|
| 1     | Linear Programming (LP)             | Classic LP problem solving production mix optimization with resource constraints.               | Completed |
| 2     | Mixed-Integer Linear Programming (MILP) | Extends LP by including integer decision variables to model discrete choices and fixed costs.    | Planned   |
| 3     | Integer Programming (IP)            | Focuses on pure integer optimization problems, such as scheduling and assignment problems.      | Planned   |
| 4     | Nonlinear Programming (NLP)         | Tackles problems with nonlinear objectives or constraints.                                      | Planned   |
| 5     | Multi-Objective Optimization        | Implements optimization with multiple conflicting objectives, using Pareto fronts, etc.         | Planned   |

---

## Projects

### 1. Linear Programming (LP)

- **Folder:** `linear_programming`
- **Description:** Production mix optimization maximizing profit with linear constraints.
- **Key Tools:** PuLP, CBC Solver
- **Status:** Completed  
- **Link:** [linear_programming](https://github.com/thiagogsdsa/mathematical-optimization-projects/tree/main/Production_Mix_Optimization)

### 2. Mixed-Integer Linear Programming (MILP)

- **Folder:** `mixed_integer_linear_programming`
- **Description:** Optimization including integer variables to model discrete decisions such as product selection, fixed costs, or scheduling.
- **Key Tools:** PuLP, CBC Solver, potentially Gurobi or CPLEX for larger instances.
- **Status:** Planned  
- **Link:** [mixed_integer_linear_programming](./mixed_integer_linear_programming)

### 3. Integer Programming (IP)

- **Folder:** `integer_programming`
- **Description:** Focused on pure integer decision variables, such as job scheduling, facility location, or combinatorial optimization.
- **Key Tools:** PuLP, CBC Solver
- **Status:** Planned  
- **Link:** [integer_programming](./integer_programming)

### 4. Nonlinear Programming (NLP)

- **Folder:** `nonlinear_programming`
- **Description:** Problems with nonlinear objectives or constraints, solved using libraries such as SciPy.optimize, IPOPT, or others.
- **Status:** Planned  
- **Link:** [nonlinear_programming](./nonlinear_programming)

### 5. Multi-Objective Optimization

- **Folder:** `multi_objective_optimization`
- **Description:** Handling problems with multiple objectives, implementing Pareto front computations, scalarization, and evolutionary algorithms.
- **Status:** Planned  
- **Link:** [multi_objective_optimization](./multi_objective_optimization)

---

## Requirements

Most projects require Python 3.7+ with specific libraries such as PuLP, NumPy, and Matplotlib. Each project folder contains its own `requirements.txt`.

Install dependencies with:

```bash
pip install -r requirements.txt
