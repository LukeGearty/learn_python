# chapter 3 practice project. This chapter covered functions and their uses


def collatz(number):
    if number == 0:
        return 0
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

def get_input():

    number = int(input("Enter a number: "))
    try:
        while number > 1:
            number = collatz(number)
            print(number)
    except ValueError:
        print(f"{number} is not a number")


get_input()