

###########
# Library #
###########

def mult_of_5(n):
    mult_5 = filter(lambda x: x % 5 == 0, range(n))
    return mult_5


def lmda_function(n):
    mult_lst = []

    range_lst = range(n)

    for i in range_lst:
        if i % 5 == 0:
            mult_lst.append(i)

    return mult_lst


lam_var = lambda x: x ** 2


def sqr(n):
    res = n ** 2
    return res

##################################
# Script / Application / Program #
##################################

def main():
    multiple_of_5 = mult_of_5(1000)
    print multiple_of_5

    lambda_function = lmda_function(1000)
    print lambda_function

    lam_variable = lam_var(4)
    print lam_variable

    the_sqr = sqr(4)
    print the_sqr


if __name__ == '__main__':
    main()
