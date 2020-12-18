#!/usr/bin/env python3
#
# Created by: Roman Cernetchi
# Created on: December 2020
# This program loops colours


def main():
    # This function loops colours

    # process

    counter1 = 0
    number = 1000

    for counter1 in range(1000, 2005):
        if number < 2004:
            print("{0}, {1}, {2}, {3}, {4}".format(number, number + 1,
                                                   number + 2, number + 3,
                                                   number + 4,
                                                   number + 5))
            number = number + 5


if __name__ == "__main__":
    main()
