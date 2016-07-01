###########
# Imports #
###########

import os
import random
import string


###########
# Library #
###########

def make_random_file(path):
    with open(path, 'w') as f:
        for i in range(100):
            f.write(''.join([random.choice(string.ascii_letters) for _ in range(80)]))
            f.write('\n')


def load_file_line(path):
    with open(path) as f:
        for line in f:
            yield line


def make_lowercase(letters):
    for letter in letters:
        yield letter.lower()


def save_letters(path, letters):
    with open(path, 'w') as f:
        for line in letters:
            f.write(line)


def read_lower_case_letters(path):
    with open(path) as f:
        for _ in f:
            lst = [line for line in f]
            res = ''.join(lst)
            return res


##########
# Script #
##########

def main():
    # IVARS - instance variables
    rando_path = os.path.join('/Users/quietdesperation/Desktop/Python - All/GitHub/Software-Engineering-Portfolio/'
                              'File_Handling', 'rando.txt')
    save_path = os.path.join('/Users/quietdesperation/Desktop/Python - All/GitHub/Software-Engineering-Portfolio/'
                             'File_Handling', 'rando_lower.txt')
    # setup
    make_random_file(rando_path)
    # load data
    letters = load_file_line(rando_path)
    # process data
    lower_case = make_lowercase(letters)
    # save data / send to database / send to web page
    save_letters(save_path, lower_case)
    print(read_lower_case_letters(save_path))


if __name__ == '__main__':
    main()
