###########
# Imports #
###########

import unittest
from projecteuler.problem_sets.problem_8 import get_highest_value, multiply_item_in_list, create_list_sets, number_split


###################
# Testing Library #
###################

class TestProjectEuler(unittest.TestCase):
    def test_x_to_the_n_power(self):
        base = 2
        exponent = 3
        expected_res = 8
        res = x_to_the_n_power(base, exponent)

        self.assertEqual(expected_res, res)

    def test_number_to_list(self):
        n = 3
        expected_res = 8
        res = number_to_list(n)

        self.assertEqual(expected_res, res)


##################
# Test Functions #
##################

if __name__ == '__main__':
    unittest.main()
