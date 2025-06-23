# Facility Location Optimization

## Overview

This project addresses a classical Mixed-Integer Linear Programming (MILP) problem: selecting optimal facility locations and assigning customer demands to them in a way that minimizes total cost. This cost includes both fixed facility-opening costs and transportation costs to customers.

---

## Problem Description

A company must decide **which facilities to open** from a set of potential locations and **how to allocate customer demand** to those facilities.

Each facility has:

- a fixed opening cost $f_i$
- a capacity limit $C_i$
- a transportation cost $c_{ij}$ to serve customer $j$

The goal is to determine the binary open/close decision variables $y_i \in \{0,1\}$ and allocation amounts $x_{ij} \geq 0$ to minimize total cost while satisfying all demands.

---

## Mathematical Model

Minimize

$$
\sum_{i=1}^m \sum_{j=1}^n c_{ij} x_{ij} + \sum_{i=1}^m f_i y_i
$$

subject to

$$
\sum_{i=1}^m x_{ij} = d_j, \quad \forall j=1,\ldots,n
$$

$$
\sum_{j=1}^n x_{ij} \leq C_i y_i, \quad \forall i=1,\ldots,m
$$

$$
x_{ij} \leq d_j y_i, \quad \forall i=1,\ldots,m, \quad j=1,\ldots,n
$$

$$
y_i \in \{0,1\}, \quad \forall i=1,\ldots,m
$$

$$
x_{ij} \geq 0, \quad \forall i=1,\ldots,m, \quad j=1,\ldots,n
$$

---

**Where:**

- $m$ = number of candidate facilities
- $n$ = number of customers
- $y_i$ = binary variable indicating if facility $i$ is opened
- $x_{ij}$ = amount shipped from facility $i$ to customer $j$
- $f_i$ = fixed cost to open facility $i$
- $c_{ij}$ = unit transportation cost from facility $i$ to customer $j$
- $d_j$ = demand of customer $j$
- $C_i$ = capacity of facility $i$

---

## Theoretical Background

This is a Mixed-Integer Linear Program (MILP), combining binary and continuous variables. MILPs are NP-hard but widely solvable in practice using solvers like CBC, Gurobi, and CPLEX. LP relaxations (allowing $y_i \in [0,1]$) can be used to obtain lower bounds.

---

## How to Run the Project

The project provides three solution methods to the Facility Location Problem:

- **Exact MILP Solver:** Uses a Mixed-Integer Linear Programming solver to find the global optimum.
- **Greedy Heuristic:** A fast, approximate solution that builds a feasible solution by allocating demands greedily.
- **Metaheuristic (Simulated Annealing):** An iterative probabilistic search to improve solutions by exploring neighbors.

By running the script `main_comparison.py`, you can execute all three methods on a chosen problem instance and compare their performance. Typical output includes the total cost and computation time for each method.

---

### Sample output from `main_comparison.py` (instance with 100 facilities and 800 customers):

The instance shown was randomly generated with 100 candidate facilities and 800 customer nodes using the included generator.

---
--- Exact MILP ---
Total cost: 400525.00
Time elapsed: 4.5944 seconds

--- Greedy Heuristic ---
Total cost: 413397.00
Time elapsed: 0.0196 seconds

--- Simulated Annealing ---
Total cost: 413145.00
Time elapsed: 2.7743 seconds


---
This output shows that while the exact solver finds the optimal cost, it takes longer. The heuristic is very fast but less optimal, and the metaheuristic balances between solution quality and time.

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
