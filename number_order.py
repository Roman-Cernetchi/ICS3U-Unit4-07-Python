#!/usr/bin/env python3
#
# Created by: Roman Cernetchi
# Created on: December 2020
# This program finds the smallest and largest


def main():
    # This function finds the smallest and largest
    # process
    while True:
        # Input
        input_amount_string = input("Enter how many numbers "
                                    "you will use: ")
        try:
            input_amount = int(input_amount_string)
            break
        except Exception:
            print("This was not an integer")

    loop_counter = 0
    largest = 0
    smallest = 99000000

    while loop_counter < input_amount:
        loop_counter = loop_counter + 1

        # Input
        while True:
            chosen_number_string = input("Enter your chosen number: ")

            try:
                chosen_number = int(chosen_number_string)
                assert chosen_number > 0
                break
            except AssertionError:
                print("Integer wasn't positive")
            except Exception:
                print("This was not an integer")

        if chosen_number > largest:
            largest = chosen_number
        if chosen_number < smallest:
            smallest = chosen_number

        if loop_counter < input_amount:
            continue

        print("")
        print("largest = {0}, smallest = {1}".format(largest, smallest))


if __name__ == "__main__":
    main()
