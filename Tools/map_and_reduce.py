###########
# Library #
###########


def get_lst_from_n(n):
    lst = range(1, n + 1)
    return lst


def multiply_n_by_2(n):
    res = n ** 9
    return res


def get_new_lst(lst):
    res = map(multiply_n_by_2, lst)
    return res


##########
# Script #
##########

def main():
    n = 10
    funnel = reduce(lambda x, y: y(x), [get_lst_from_n, get_new_lst], n)
    print(funnel)


if __name__ == '__main__':
    main()
