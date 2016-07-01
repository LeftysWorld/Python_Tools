###########
# Imports #
###########

import unittest
from Project_Euler.problem_sets.problem_6 import get_numbers_under_n, square_numbers, sum_squared, squared_sums, \
    sum_squared_difference

###################
# Testing Library #
###################


class TestProjectEuler(unittest.TestCase):
    def test_get_numbers_under_n(self):
        n = 5
        expected_res = [1, 2, 3, 4, 5]
        res = get_numbers_under_n(n)

        self.assertEqual(expected_res, res)

    def test_square_numbers(self):
        n = 5
        expected_res = 25
        res = square_numbers(n)

        self.assertEqual(expected_res, res)

    def test_sum_squared(self):
        lst = [1, 2, 3, 4, 5]
        expected_res = 55
        res = sum_squared(lst)

        self.assertEqual(expected_res, res)

    def test_squared_sums(self):
        lst = [1, 2, 3, 4, 5]
        expected_res = 225
        res = squared_sums(lst)

        self.assertEqual(expected_res, res)

    def test_sum_squared_difference(self):
        squared_sums = 225
        sum_squared = 55
        expected_res = 170
        res = sum_squared_difference(squared_sums, sum_squared)

        self.assertEqual(expected_res, res)


##################
# Test Functions #
##################

if __name__ == '__main__':
    unittest.main()
