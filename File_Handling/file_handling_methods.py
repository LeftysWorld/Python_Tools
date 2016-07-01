###########
# Imports #
###########

import os
from pprint import pprint
import random
import string


###########
# Library #
###########

def load_file_all(path):
    with open(path) as file_object:
        res = file_object.read()
        return res


def traditional_file_handling_2(path):
    f = open(path)
    res = f.read()
    return res


def traditional_file_handling(path):
    # must specify
    f = open(path, 'r')
    try:
        res = f.read()
        return res
    finally:
        f.close()


def simple_list():
    res = [i for i in range(80)]
    return res


def list_comp(n):
    lst = [i for i in range(n)]
    return lst


def load_file_line(path):
    with open(path) as f:
        for line in f:
            yield line


def load_file_chunks(path, chunksize=1024):
    with open(path) as f:
        while True:
            nxt_chunk = f.read(chunksize)
            if not nxt_chunk:
                raise StopIteration
            yield nxt_chunk


def make_random_file(path):
    """
    Make a file of random letters
    :return: None
    """
    with open(path, 'w') as f:
        for i in range(100):
            # write a line of random letters to file
            f.write(''.join([random.choice(string.ascii_letters) for _ in range(80)]))
            # make a new line
            f.write('\n')


def make_lowercase(letters):
    for letter in letters:
        res = letter.lower()
        yield res


def save_letters(path, letters):
    with open(path, 'w') as f:
        for line in letters:
            f.write(line)


def workflow():
    # IVARS - instance variables
    rando_path = os.path.join('/Users/quietdesperation/Desktop/Python - All/GitHub/Software-Engineering-Portfolio/'
                              'File_Handling/', 'rando.txt')
    save_path = os.path.join('/Users/quietdesperation/Desktop/Python - All/GitHub/Software-Engineering-Portfolio/'
                             'File_Handling/', 'rando_lower.txt')
    # setup
    make_random_file(rando_path)
    # load data
    letters = load_file_line(rando_path)
    # process data
    lower_case = make_lowercase(letters)
    # save data / send to database / send to web page
    save_letters(save_path, lower_case)


##########
# Script #
##########

def main():
    workflow()


def test():
    path = '/Users/quietdesperation/Desktop/Python - All/GitHub/Software-Engineering-Portfolio/File_Handling/rando.txt'
    print(load_file_all(path))
    pprint(list(load_file_line(path)))
    pprint(list(load_file_chunks(path)))
    print(traditional_file_handling(path))

if __name__ == '__main__':
    main()
    test()
