###########
# Library #
###########


def foo():
    my_dict = dict(n=42, name="taco")
    s = "{n:.^10}{name:5}".format(**my_dict)
    return s


##########
# Script #
##########

def main():
    print(foo())


if __name__ == '__main__':
    main()