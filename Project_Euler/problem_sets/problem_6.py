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
    res = sum(map(square_numbers, lst))
    return res


def squared_sums(lst):
    res = sum(lst) ** 2
    return res


def sum_squared_difference(squared_sum, sum_square):
    res = squared_sum - sum_square
    return res


##########
# Script #
##########

def main():
    n = 100
    get_numbers = get_numbers_under_n(n)
    difference_of_sum_and_squared = sum_squared_difference(squared_sums(get_numbers), sum_squared(get_numbers))
    print(difference_of_sum_and_squared)


if __name__ == '__main__':
    main()
