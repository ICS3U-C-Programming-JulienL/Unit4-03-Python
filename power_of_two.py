#!/usr/bin/env python3

# Created By: Julien Lamoureux
# Date: November 13, 2023
# This program displays all the numbers from 0 to the user's number squared


def main():
    # get the user number as a string
    print("This program displays all the numbers from 0 to the user's number squared.")
    user_num_string = input("Enter your integer: ")

    # initialize power_product to 0
    power_product = 0

    try:
        # convert user number to an integer
        user_num_int = int(user_num_string)

        # if the user number is less than 0, tell the user to enter a positive integer
        if user_num_int < 0:
            print("{} is not a positive integer".format(user_num_string))
        else:
            # otherwise while the counter is less than or equal to the user number:
            for counter in range(user_num_int + 1):
                # multiply the counter to the factorial
                power_product = counter**2

                # display all the numbers from 0 to the user's number squared
                print("{0}^2 = {1}".format(counter, power_product))

    except:
        # if the number is not an integer, then tell them their input is invalid
        print(
            "\n{} is not a valid integer. Please enter a positive integer.".format(
                user_num_string
            )
        )


if __name__ == "__main__":
    main()
