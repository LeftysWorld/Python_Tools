###########
# Imports #
###########

import unittest
from projecteuler.problem_sets.problem_2 import fibonacci_numbers, sum_of_even_fibonacci_numbers


###################
# Testing Library #
###################

class TestProjectEuler(unittest.TestCase):
    def test_new_fibonacci(self):
        start = 1
        end = 5
        expected_res = [1, 1, 2, 3, 5]
        res = new_fibonacci(start, end)

        self.assertEqual(expected_res, res)

    def test_project_2_even_fibonacci_numbers(self):
        lst = [1, 1, 2, 3, 5]
        expected_res = 2
        res = sum_of_even_fibonacci_numbers(lst)

        self.assertEqual(expected_res, res)


##################
# Test Functions #
##################

if __name__ == '__main__':
    unittest.main()