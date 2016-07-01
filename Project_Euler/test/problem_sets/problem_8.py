###########
# Imports #
###########

import unittest


###################
# Testing Library #
###################
from Project_Euler.problem_sets.problem_8 import split_number_to_list, create_list_sets, get_highest_value, \
    multiply_item_in_list


class TestProjectEuler(unittest.TestCase):
    def test_split_number_to_list(self):
        n = 2345
        expected_res = [2,3,4,5]
        res = split_number_to_list(object)

        self.assertEqual(expected_res, res)

    def test_create_list_sets(self):
        lst = [2,3,4,5]
        n = 3
        expected_res = [[2,3,4],[3,4,5]]
        res = create_list_sets(lst, n)

        self.assertEqual(expected_res, res)

    def test_multiply_item_in_list(self):
        lst = [2, 3, 4, 5]
        expected_res = 120
        res = multiply_item_in_list(lst)

        self.assertEqual(expected_res, res)


##################
# Test Functions #
##################

if __name__ == '__main__':
    unittest.main()
