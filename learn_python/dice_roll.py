import random
import sys

def roll_dice(dice):
    return random.randint(1, dice)


def main():
    if len(sys.argv) == 3:
        dice = int(sys.argv[1])
        num_of_times = int(sys.argv[2])
        sum = 0
        if num_of_times > 1:
            for _ in range(num_of_times):
                curr = roll_dice(dice)
                sum+=curr
                print(curr)
            print(f"Sum of rolls: {sum}")
        else:
            print(roll_dice(dice))
    else:
        print("Invalid syntax")
        print("python3 dice_roll.py <numOfDice> <numOfTimes>")


if __name__=="__main__":
    main()