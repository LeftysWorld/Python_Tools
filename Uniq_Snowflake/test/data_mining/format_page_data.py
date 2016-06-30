###########
# Imports #
###########

import os
import unittest
from Uniq_Snowflake.data_mining.format_page_data import open_file, file_with_split_lines, create_list, get_dict_keys, \
    get_dict_values, list_of_dictionaries


###################
# Testing Library #
###################

class TestFormatPageData(unittest.TestCase):
    def test_open_file(self):
        path = os.path.join(os.path.dirname(__file__), 'TEST_FILE.txt')
        expected_res = "This is a test file"
        res = open_file(path)

        self.assertEqual(expected_res, res)

    def test_file_with_split_lines(self):
        contents = "test\n test test\n"
        expected_res = ['test\n test test\n']
        res = file_with_split_lines(contents)

        self.assertEqual(expected_res, res)

    def test_create_list(self):
        split_lines = "test\n test\n\n"
        expected_res = [['t'], ['e'], ['s'], ['t'], [''], [' '], ['t'], ['e'], ['s'], ['t'], ['']]
        res = create_list(split_lines)

        self.assertEqual(expected_res, res)

    def test_get_dict_keys(self):
        lst = [['a', 'b', 'c', ''], ['d', 'e', 'f'], ['g', 'h', 'i']]
        expected_res = ['a', 'b', 'c']
        res = get_dict_keys(lst)

        self.assertEqual(expected_res, res)

    def test_get_dict_values(self):
        lst = [['a', 'b', 'c', ''], ['d', 'e', 'f'], ['g', 'h', 'i']]
        expected_res = [['d', 'e', 'f'], ['g', 'h', 'i']]
        res = get_dict_values(lst)

        self.assertEqual(expected_res, res)

    def test_list_of_dictionaries(self):
        keys_list = ['a', 'b', 'c']
        values_list = [['d', 'e', 'f'], ['g', 'h', 'i']]
        expected_res = [{'a': 'd', 'b': 'e', 'c': 'f'}, {'a': 'g', 'b': 'h', 'c': 'i'}]
        res = list_of_dictionaries(keys_list, values_list)

        self.assertEqual(expected_res, res)


##################
# Test Functions #
##################

if __name__ == '__main__':
    unittest.main()
