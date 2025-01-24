## user has unlimited attempts to guess an number

import random
import math


def get_random_number():
    return random.randint(1, 100)


def get_number_from_user():
    return int(input("Enter a number between 1 and 100: "))


def is_number_in_range(number):
    return 1 <= number <= 100


def is_number_correct(number, random_number):
    return number == random_number


def help_find_number(number, random_number):
    num = random_number - number
    if num > 0:

        if num < 5:
            print("Red hot.")
        elif num < 10:
            print("Hot.")
        elif num < 20:
            print("Warm.")
        else:
            print("Cold.")
    else:
        if num > -5:
            print("Red hot.")
        elif num > -10:
            print("Hot.")
        elif num > -20:
            print("Warm.")
        else:
            print("Cold.")


def get_number_of_attempts():
    return math.ceil(math.log(100, 2))


while True:
    random_number = get_random_number()
    print("----------I have thought of a number between 1 and 100.----------")
    print("You have 10 attempts to guess it.")

    for i in range(10):
        number = get_number_from_user()

        # if number == 'x':
        #     break

        if not is_number_in_range(number):
            print(f"Please enter a number between 1 and 100.({10 - i} attempts left)")
            continue

        if is_number_correct(number, random_number):
            print("You guessed it!")
            break
        else:
            print(f"({10 - (i + 1)} attempts left)")
            help_find_number(number, random_number)
    else:
        print("You have run out of attempts. The number was", random_number)
