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
    n = 100
    funnel = reduce(lambda x, y: y(x), [factorial, number_to_list, count_list], n)
    print(funnel)

if __name__ == '__main__':
    main()
