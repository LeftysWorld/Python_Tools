
###########
# Imports #
###########

import unittest


###################
# Testing Library #
###################

url_data = "[<html><head></head><body><h1>Test</h1><p>Test</p><tr><td>Testing</td></tr></body></html>]"


class TestScrapePage(unittest.TestCase):

    def test_get_soup_body(self):
        test_data = url_data
        expected_res = "[<tr><td>Testing</td></tr>]"
        res = repr(get_soup_body(test_data)

        self.assertEqual(expected_res, res)

    def test_extract_data(self):
        sample_input = ['<tr>\xa0<h1>keyThis</h1>\xc2<h4>view\xc2\xa0book\xc2\xa0info</h4><h5>Test Passes</h5></tr>']
        expected_res = ['This Test Passes']
        res = list(extract_data(sample_input))

        self.assertEqual(expected_res, res)


##################
# Test Functions #
##################

if __name__ == '__main__':
    unittest.main()
