import random

def create_deck():
    deck = []

    suits = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    for suit in suits:
        for card in cards:
            current_card = f"{card} of {suit}"
            deck.append(current_card)

    return deck

def assign_values(deck: list, aces_high: bool):
    values = {}

    for card in deck:
        split_card = card.split()
        if split_card[0].isdigit():
            values[card] = int(split_card[0])
        elif split_card[0] == "Jack" or split_card[0] == "Queen" or split_card[0] == "King":
            values[card] = 10
        else: # is an Ace
            if aces_high:
                values[card] = 11
            else:
                values[card] = 1
    
    return values


def play(deck: list, values: dict):
    hand = []
    hand_value = 0

    card_one = random.choice(deck)
    hand.append(card_one)
    deck.remove(card_one)
    card_two = random.choice(deck)
    deck.remove(card_two)
    hand.append(card_two)
    hand_value = hand_value + values[card_one] + values[card_two]

    if hand_value == 21:
        print(f"You drew the {card_one} and {card_two}, to get {hand_value}! My turn!")
        return hand_value
    
    print(f"You drew the {card_one} and {card_two}. Your hand has a value of {hand_value}. What do you do?")
    print("1. Hit Me")
    print("2. Stand")
    choice = int(input("1 or 2: "))

    while choice == 1 and hand_value < 21 and len(deck) > 0:
        if len(deck) == 0:
            print("The deck is empty! No more cards can be drawn")
            break
        card = random.choice(deck)
        deck.remove(card)
        hand.append(card)
        hand_value += values[card]
        if hand_value < 21:
            print(f"You drew the {card}. You now have a value of {hand_value}. What do you do?")
            print("1. Hit Me")
            print("2. Stand")
            choice = int(input("1 or 2:" ))
        elif hand_value == 21:
            print(f"You drew the {card}. You now have a value of {hand_value}. My turn!")
            break
        else:
            print(f"You drew the {card}. You now have a hand value of {hand_value}. You might lose, but we'll see.")
            break
    
    return hand_value


def computer_play(deck: list, values: dict):
    hand = []
    hand_value = 0
    card_one = random.choice(deck)
    deck.remove(card_one)
    card_two = random.choice(deck)
    deck.remove(card_two)
    hand_value += values[card_one] + values[card_two]
    hand.append(card_one)
    hand.append(card_two)

    print(f"I drew the {card_one} and {card_two}. My hand is now at {hand_value}")
    max_hand = 18 # the maximum amount the computer will want the hand to go to

    while hand_value < max_hand and hand_value < 21 and len(deck) > 0:
        if len(deck) == 0:
            print("The deck is empty! No more cards can be drawn")
            break
        card = random.choice(deck)
        deck.remove(card)
        hand_value += values[card]
        print(f"I drew the {card}. My hand value is now {hand_value}")
        if hand_value == 21:
            break
        if hand_value > 21:
            print(f"I busted with a hand value of {hand_value}!")
            break

    return hand_value

def check_winner(player_hand: int, computer_hand: int):

    if player_hand > 21 and computer_hand <= 21:
        winner = "computer"
    elif player_hand <= 21 and computer_hand > 21:
        winner = "player"
    elif player_hand < 21 and computer_hand < 21:
        if player_hand > computer_hand:
            winner = "player"
        else:
            winner = "computer"
    elif player_hand == 21 and computer_hand != 21:
        winner = "player"
    elif player_hand != 21 and computer_hand == 21:
        winner = "computer"
    elif player_hand == 21 and computer_hand == 21:
        winner = None
    elif player_hand > 21 and computer_hand > 21:
        winner = "computer"
    

    return winner

def get_input(prompt, valid_choices):
    while True:
        try:
            choice = int(input(prompt))
            if choice in valid_choices:
                return choice
            else:
                print(f"Please enter a valid choice: {valid_choices}")
        except ValueError:
            print("Invalid Input, please enter a number")

def main():
    aces = get_input("Are aces high or low this round? 1 = High, 2 = Low: ", [1, 2])
    if aces == 1:
        aces_high = True
    else:
        aces_high = False
    deck = create_deck()
    values = assign_values(deck, aces_high)

    player_value = play(deck, values)

    print(f"Your hand is at {player_value}. My turn!")

    computer_value = computer_play(deck, values)

    print(f"My hand value is {computer_value}")

    winner = check_winner(player_value, computer_value)

    if winner == "player":
        print("You win!")
    elif winner == "computer":
        print("I won!")
    else:
        print("It is a tie!")

if __name__=="__main__":
    main()