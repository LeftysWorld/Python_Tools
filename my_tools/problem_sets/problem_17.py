"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115
(one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""


###########
# Library #
###########

def get_number(n):
    return n


def split_number(n):
    string_the_number = str(n)
    lst = [int(digit) for digit in string_the_number]
    my_list = lst[::-1]
    return my_list


def get_words(n):
    split = split_number(n)
    split_units = split[0]
    if n > 19:
        split_tens = split[1]
        under_twenty = int(str(split_tens) + str(split_units))

    units = ["zero", "one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen",
             "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    greater = ["hundred", "thousand"]

    def under_100(n):
        if len(split) <= 2 and n < 20:
            unit = units[n]
            return unit
        if len(split) > 2 and under_twenty < 20:
            unit = units[under_twenty]
            return unit
        elif n > 19 and split_units == 0:
            ten = tens[split_tens - 2]
            return ten
        elif n > 19 and split_units != 0:
            unit = units[split_units]
            ten = tens[split_tens - 2]
            res = ten + unit
            return res

    under_hundred = under_100(n)

    def under_1001(n):
        if n == 1000:
            thousand = "onethousand"
            return thousand
        elif len(split) == 3 and split_tens == 0 and split_units == 0:
            number = split[2]
            res = units[number] + greater[0]
            return res
        elif len(split) == 3:
            number = split[2]
            res = units[number] + greater[0]
            results = res + "and" + under_hundred
            return results
        else:
            res = under_hundred
            return res

    under_thousand = under_1001(n)
    return under_thousand


def get_list(n):
    lst = [get_words(n + 1) for n in xrange(n)]
    return lst


def count_letters(lst):
    total = 0
    for i in lst:
        total += len(i)
    return total


##################################
# Script / Application / Program #
##################################

def main():
    problem_17_setup = get_number(1000)
    problem_17_get_words = get_words(problem_17_setup)
    problem_17_get_list = get_list(problem_17_setup)
    problem_17_count_letters = count_letters(problem_17_get_list)
    print problem_17_count_letters


if __name__ == '__main__':
    main()
