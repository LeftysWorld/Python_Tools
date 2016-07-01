###########
# Imports #
###########


import unittest
from Project_Euler.problem_sets.problem_20 import factorial, number_to_list, count_list

###################
# Testing Library #
###################


class TestProjectEuler(unittest.TestCase):
    def test_factorial(self):
        n = 4
        expected_res = 24
        res = factorial(n)

        self.assertEqual(expected_res, res)

    def test_number_to_list(self):
        n = 24
        expected_res = [2, 4]
        res = number_to_list(n)

        self.assertEqual(expected_res, res)

    def test_count_list(self):
        lst = [2, 4]
        expected_res = 6
        res = count_list(lst)

        self.assertEqual(expected_res, res)


##################
# Test Functions #
##################

if __name__ == '__main__':
    unittest.main()
