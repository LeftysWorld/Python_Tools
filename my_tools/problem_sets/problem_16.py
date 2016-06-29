"""
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
"""

###########
# Library #
###########


def x_to_the_n_power(x, n):
    power = x ** n
    return power


def number_to_list(n):
    string_the_number = str(n)
    lst = [int(digit) for digit in string_the_number]
    return lst


def add_res(lst):
    res = sum(lst)
    return res


##################################
# Script / Application / Program #
##################################

def main():
    problem_16_x_to_the_n_power = x_to_the_n_power(2, 1000)
    problem_16_number_to_list = number_to_list(problem_16_x_to_the_n_power)
    problem_16_add_res = add_res(problem_16_number_to_list)
    print problem_16_add_res


if __name__ == '__main__':
    main()
