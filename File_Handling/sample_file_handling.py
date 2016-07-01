###########
# Imports #
###########

from pprint import pprint


###########
# Library #
###########

def load_file(path):
    with open(path) as f:
        res = f.read()
        return res


def load_file_chunks(path, chunk_size=1024):
    """load large file"""
    with open(path) as f:
        while True:
            nxt_chunk = f.read(chunk_size)
            if not nxt_chunk:
                raise StopIteration
            yield nxt_chunk


def load_file_line(path):
    with open(path) as f:
        for line in f:
            yield line


def make_loop(lines):
    res = [item.strip() for item in lines]
    return res


##########
# Script #
##########

def main():
    path = r"/Users/quietdesperation/Desktop/Python - All/GitHub/Software-Engineering-Portfolio/File_Handling/path.txt"
    # print(load_file(path))
    # print(list(load_file_chunks(path)))
    # pprint(list(load_file_line(path)))
    pprint(make_loop(load_file_line(path)))


if __name__ == '__main__':
    main()
