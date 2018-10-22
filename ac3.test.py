import unittest
from ac3 import CSPSolver


class TestAC3(unittest.TestCase):
    def test_three_variables(self):
        # arcs, domains, and constraints
        arcs = [('a', 'b'), ('b', 'a'), ('b', 'c'), ('c', 'b'), ('c', 'a'), ('a', 'c')]

        domains = {
            'a': [2, 3, 4, 5, 6, 7],
            'b': [4, 5, 6, 7, 8, 9],
            'c': [1, 2, 3, 4, 5]
        }

        # constraints:
        # b = 2*a
        # a = c
        # b >= c - 2
        # b <= c + 2
        constraints = {
            ('a', 'b'): lambda a, b: a * 2 == b,
            ('b', 'a'): lambda b, a: b == 2 * a,
            ('a', 'c'): lambda a, c: a == c,
            ('c', 'a'): lambda c, a: c == a,
            ('b', 'c'): lambda b, c: b >= c - 2,
            ('b', 'c'): lambda b, c: b <= c + 2,
            ('c', 'b'): lambda c, b: b >= c - 2,
            ('c', 'b'): lambda c, b: b <= c + 2
        }

        expected = { 'a': [2], 'b': [4], 'c': [2] }
        solver = CSPSolver(arcs, domains, constraints)
        result = solver.solve()

        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
