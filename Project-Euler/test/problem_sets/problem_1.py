###########
# Imports #
###########

import unittest
from projecteuler.problem_sets.problem_1 import get_numbers_under_n, get_real_numbers


###################
# Testing Library #
###################

class TestProjectEuler(unittest.TestCase):
    def test_multiples_of_3_and_5(self):
        n = 5
        expected_res = 3
        res = multiples_of_3_and_5(n)

        self.assertEqual(expected_res, res)


##################
# Test Functions #
##################

if __name__ == '__main__':
    unittest.main()
