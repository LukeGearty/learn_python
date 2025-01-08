import sys

def get_name():
    player_name = input("What is your character's name?: ")

    #TO DO: code a way to generate a random name if the player wants to get a random name
    return player_name


def greet_player(player_name):
    print(f"Welcome {player_name} to the wonderful world of Azala! Are you ready to go on your adventure? 1 to continue, 2 to exit: ")

    while True:
        try:
            choice = int(input())
            if choice == 1:
                return True
            elif choice == 2:
                return False
            else:
                print("Please enter a valid response: 1 or 2")
        except ValueError:
            print("Invalid choice, enter a number")


def main_hall():
    print("You find yourself in a dark castle, walking along to see there are two hallways, left and right.\n")
    print("Which door do you choose? Left (1) or Right (2)")
    while True:
        try:
            choice = int(input())
            if choice == 1:
                return "left"
            elif choice == 2:
                return "right"
            else:
                print("Please enter a valid response: 1 or 2")
        except ValueError:
            print("Invalid choice, enter a number")


def left_door():
    print("You find yourself in an empty hallway. Nothing is in this hallway, or so it seems.")
    print("What do you do?")
    #explore further
    print("1. Explore the hallway")
    #go back to the starting area
    print("2. Go back the way you came")
    while True:
        try:
            choice = int(input())
            if choice == 1:
                print("Upon further exploration of the hallway, you find a secret compartment. Reaching in to the compartment, you discover a golden sword. You turn around the way you came with a sword in hand.")
                return True #player now has sword
            elif choice == 2:
                print("You go back the way you came.")
                return False #player does not have sword
            else:
                print("Invalid choice")
        except ValueError:
            print("Invalid choice, please pick a number")

def right_door(has_sword):
    print("You go down a long hallway and find a massive door a few steps away. With little else to do, you push the door open and are greeted face to face with a fire breathing dragon, who is rather peeved that you disturbed his slumber.")
    print("What do you do?")
    print("1. Fight the dragon")
    print("2. Run away")

    while True:
        try:
            choice = int(input())
            if choice == 1:
                if has_sword:
                    print("After a fearsome battle, you manage to slay the dragon with the golden sword and steal all the treasure. Well done!")
                    return True #player wins
                else:
                    print("After a quick battle, the dragon has you for lunch. The End!")
                    return False #player loses
            elif choice == 2:
                print("You rather bravely run away from the dragon, back into the hall where you started")
                main_hall()
                return None #player retreats
        except ValueError:
            print("Invalid choice, please pick a number")


def main():
    print("Welcome to the Text Adventure Game")
    player_name = get_name()
    if not greet_player(player_name):
        return
    
    has_sword = False

    while True:
        choice = main_hall()
        if choice == "left":
            has_sword = left_door() or has_sword
        elif choice == "right":
            result = right_door(has_sword)
            if result is True: 
                print("You win!")
                sys.exit()
            elif result is False:
                print("You lose!")
                sys.exit()

    

if __name__=="__main__":
    main()