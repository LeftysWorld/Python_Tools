"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


###########
# Library #
###########


def get_real_numbers_lst_comp(n):
    lst = [x for x in range(n) if x % 3 == 0 or x % 5 == 0]
    res = sum(lst)
    return res


##################################
# Script / Application / Program #
##################################

def main():
    problem_1 = get_real_numbers_lst_comp(1000)
    print problem_1


if __name__ == '__main__':
    main()
