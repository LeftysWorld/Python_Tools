"""
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
"""

###########
# Library #
###########


def x_to_the_n_power(base, exponent):
    power = base ** exponent
    return power


def number_to_list(n):
    lst = [int(digit) for digit in str(n)]
    res = sum(lst)
    return res


##########
# Script #
##########

def main():
    base = 2
    exponent = 1000
    _x_to_the_n_power = x_to_the_n_power(base, exponent)
    print number_to_list(_x_to_the_n_power)


if __name__ == '__main__':
    main()
