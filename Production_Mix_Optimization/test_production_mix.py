import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from production_mix import solve_production_mix

class TestProductionMix(unittest.TestCase):
    def setUp(self):
        self.products = ['A', 'B']
        self.profits = {'A': 10, 'B': 20}
        self.requirements = {
            'A': {'R1': 1, 'R2': 2},
            'B': {'R1': 3, 'R2': 1}
        }
        self.limits = {'R1': 10, 'R2': 10}

    def test_solution_keys(self):
        result, _ = solve_production_mix(self.products, self.profits, self.requirements, self.limits)
        self.assertSetEqual(set(result.keys()), set(self.products))

    def test_non_negative(self):
        result, _ = solve_production_mix(self.products, self.profits, self.requirements, self.limits)
        for qty in result.values():
            self.assertGreaterEqual(qty, 0)

if __name__ == '__main__':
    unittest.main()