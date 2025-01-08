import random
import sys

BOARD_SIZE = 4


def create_board():
    board = []
    #create the board with all 0s initially
    for _ in range(BOARD_SIZE):
        curr_row = []
        for x in range(BOARD_SIZE):
            curr_row.append(0)
        board.append(curr_row)
    
    #adding the new twos
    for _ in range(2):
        add_new_number(board, 2)
    return board


#can either be 2 or 4
def add_new_number(board, num):
    r = random.randint(0, 3)
    c = random.randint(0, 3)
    while board[r][c] != 0:
        r = random.randint(0, 3)
        c = random.randint(0, 3)
    board[r][c] = num


def print_board(board):
    for row in board:
        print(row)

#changing the board after every turn
#moving based on left/right
#the following functions will be for left/right movements


#check_line_row is meant to move all
def check_line_row(row, direction):
    #these two lines gather all the non_zeroes and zeroes into seperate lists
    non_zeroes = [x for x in row if x != 0]
    zeroes = [0] * (len(row) - len(non_zeroes))
    if direction == "left":
        #moving to the left, non_zeroes + zeroes. For example, if the original row is [0, 2, 2, 0], then the new row will be
        #[2, 2, 0, 0]
        slid_row = non_zeroes + zeroes
        #handling logic to make sure that adjacent numbers, if they are the same, are merged together. This will turn the example
        #above into [4, 0, 0, 0]
        merge_adjacent_numbers_row(slid_row)
        #redoing the non_zeroes and zeroes list
        non_zeroes = [x for x in slid_row if x != 0]
        zeroes = [0] * (len(row) - len(non_zeroes))
        return non_zeroes + zeroes
    elif direction == "right":
        #much of the same as above, except it would be zeroes on the left and non_zeroes on the right
        slid_row = zeroes + non_zeroes
        merge_adjacent_numbers_row(slid_row)
        non_zeroes = [x for x in slid_row if x != 0]
        zeroes = [0] * (len(row) - len(non_zeroes))
        return zeroes + non_zeroes


#merging the lines
def merge_adjacent_numbers_row(slid_line):
    for i in range(len(slid_line) - 1):
        if slid_line[i] == slid_line[i + 1] and slid_line[i] != 0:
            slid_line[i] *= 2
            slid_line[i + 1] = 0 #replacing that line with a 0
    return slid_line

#calling the function
def slide_row(board, direction):
    for i in range(len(board)):
        board[i] = check_line_row(board[i], direction)
    return board


#for up and down directions

def slide_col(board, direction):
    # Transpose the board so that columns become rows
    transposed_board = [list(x) for x in zip(*board)]
    
    # Apply slide_row logic to the transposed board
    if direction == "up":
        transposed_board = slide_row(transposed_board, "left")
    elif direction == "down":
        transposed_board = slide_row(transposed_board, "right")
    
    # Transpose the board back to restore original orientation
    new_board = [list(x) for x in zip(*transposed_board)]
    #modify the original board
    for i in range(len(board)):
        board[i] = new_board[i]
    return board

# check winning conditions
def check_win(board):
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] == 2048:
                return True
    return False


#check losing conditions
def check_loss(board):
    #if there is a 0, there technically will not be a loser
    for row in board:
        if 0 in row:
            return False
    
    #if there are no merges
    for row in board:
        for i in range(len(row) - 1):
            if row[i] == row[i + 1]:
                return False
    
    for col in range(len(board)):
        for row in range(len(board) - 1):
            if board[row][col] == board[row + 1][col]:
                return False
    
    return True

def explain_commands():
    print("'W' or 'w' to move up")
    print("'A' or 'a' to move left")
    print("'S' or 's' to move down")
    print("'D' or 'd' to move right")
    print("'Q' or 'q' to exit the game")


def play():
    print("Welcome to 2048")
    explain_commands()
    board = create_board()
    print_board(board)

    win = False
    while True:
        move = input()

        while move not in ['a', 'w', 'd', 's', 'q']:
            move = input("Enter a valid input please: ")
        if move.lower() == 'a':
            slide_row(board, "left")
        elif move.lower() == 'w':
            slide_col(board, "up")
        elif move.lower() == 'd':
            slide_row(board, "right")
        elif move.lower() == 's':
            slide_col(board, "down")
        elif move.lower() == 'q':
            break
        
        #add a new number
        add_new_number(board, random.choice([2, 4]))
        #a couple of checks
        if (check_win(board)):
            print("You win!")
            win = True
            break
        if (check_loss(board)):
            print("You Lose!")
            break 
        print_board(board)
    
    print_board(board)
    if win:
        print("Congratulations")
    else:
        print("Better luck next time")
    
    sys.exit()


def main():
    play()
    
if __name__=="__main__":
    main()