# coding=utf-8
"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

###########
# Imports #
###########

import math


###########
# Library #
###########

# Problem 20
def factorial(n):
    res = math.factorial(n)
    return res


def number_to_list(n):
    string_the_number = str(n)
    lst = [int(digit) for digit in string_the_number]
    return lst


def count_list(lst):
    total = sum(lst)
    return total


##################################
# Script / Application / Program #
##################################

def main():
    problem_20_setup = factorial(100)
    problem_20_number_to_list = number_to_list(problem_20_setup)
    problem_20_count_list = count_list(problem_20_number_to_list)
    print problem_20_count_list


if __name__ == '__main__':
    main()
