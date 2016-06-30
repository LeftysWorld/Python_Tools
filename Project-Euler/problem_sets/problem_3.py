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


##########
# Script #
##########

def main():
    n = 55143
    print(get_prime_list_from_n(n))


if __name__ == '__main__':
    main()
