#!/usr/bin/env python3
# Created by Marc Coffi
# Created in April 2022
# Power of two


def main():
    # Ask user to input a whole number
    user_input = input("Enter a whole number: ")
    print("")
    try:
        # Casting user input
        user_num = int(user_input)
        if user_num >= 0:
            # For loop to find and display the square of zero up to the number inputed by the user
            for counter in range(user_num + 1):
                print("{}^2 = {}".format(counter, counter**2))

        else:
            exit()
    # If user input a invalid value or a negative number
    except:
        print("Invalid input.\nNot a proper number")
        exit()
    # Thanks message
    print()
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
