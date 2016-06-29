# coding=utf-8
"""
The sum of the squares of the first ten natural numbers is,

12 + 22 +  + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 +  + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers
and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


###########
# Library #
###########

def get_numbers_under_n(n):
    lst = [i + 1 for i in range(n)]
    return lst


def square_numbers(n):
    res = n ** 2
    return res


def sum_squared(lst):
    new_list = map(square_numbers, lst)
    res = sum(new_list)
    return res


def squared_sums(lst):
    added = sum(lst)
    res = added ** 2
    return res


def sum_squared_difference(squared_sum, sum_square):
    res = squared_sum - sum_square
    return res


##################################
# Script / Application / Program #
##################################

def main():
    problem_6_lst = get_numbers_under_n(100)
    problem_6_sum_squared = sum_squared(problem_6_lst)
    problem_6_squared_sums = squared_sums(problem_6_lst)
    problem_6_results = sum_squared_difference(problem_6_squared_sums, problem_6_sum_squared)
    print problem_6_results


if __name__ == '__main__':
    main()
