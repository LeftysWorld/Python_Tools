"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


###########
# Library #
###########

def get_prime_list_from_n(n):
    prime_number = 1
    x = 2
    while x <= n:
        for i in xrange(2, x):  # start, stop, step
            if x % i == 0:
                x += 1
        if x < n: prime_number = x
        x += 1
    else:
        return prime_number


##################################
# Script / Application / Program #
##################################

def main():
    prime_number_setup = get_prime_list_from_n(55143)
    print prime_number_setup


if __name__ == '__main__':
    main()
