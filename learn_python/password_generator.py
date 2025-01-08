import random
from words import words


def generate_password():
    words_amount = 4
    words_used = []
    result = ""

    for i in range(words_amount):
        current_word = random.choice(words)
        while current_word in words_used:
            current_word = random.choice(words)
        result += current_word.capitalize()
    
    return result


def main():
    my_new_password = generate_password()
    print(my_new_password)


if __name__=="__main__":
    main()