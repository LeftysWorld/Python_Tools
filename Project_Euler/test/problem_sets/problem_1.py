###########
# Imports #
###########

import unittest
from Project_Euler.problem_sets.problem_1 import multiples_of_3_and_5


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
