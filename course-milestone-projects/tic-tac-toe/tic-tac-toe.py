import random

# sample board
board = ['O','X','O','X','O','X','O','X','O']
acceptable_choices = ['X','O']

def display_board(board, wonCombo = None):
    print("Current Board:")
    
    for i in range(0, 9, 3):
        c1=cell_str(board[i], wonCombo and i in wonCombo)
        c2=cell_str(board[i+1], wonCombo and i+1 in wonCombo)
        c3=cell_str(board[i+2], wonCombo and i+2 in wonCombo)
        print(f"{c1}|{c2}|{c3}")
        if i < 6:
            print("---+---+---")

def cell_str(val, highlight):
    if highlight:
        return f"[{val}]".center(3)  # highlight with []
    return f" {val} ".center(3)

# display_board(board)

def player_input(player):
    choice = 'wrong'

    while choice not in acceptable_choices:
        choice = input(f"Please pick a marker 'X' or 'O' for {player}: ")

    otherChoice = acceptable_choices[0]
    if acceptable_choices[0] == choice:
        otherChoice = acceptable_choices[1]

    print(f"{player}'s choice: {choice} & Other Player's choice: {otherChoice}")
    return (choice, otherChoice)

def place_marker(board, marker, position):
    if position not in range(1, 10):
        print(f"position is out of range: {position}")
    if marker not in acceptable_choices:
        print(f"invalid choice: {marker}")
    board[position - 1] = marker

def win_check(board, mark):
    # winning combinations (indices for 3x3)
    winning_indices = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # cols
        [0,4,8], [2,4,6]            # diagonals
    ]

    wonCombo = None
    for combo in winning_indices:
        if all(board[i] == mark for i in combo):
            wonCombo = combo
            break

    return wonCombo


def choose_first():
    return str(random.randint(1,2))

def space_check(board, position):
    return board[position - 1] == ' '

def player_choice(board):
    choice = 'wrong'

    while choice not in range(1,10):
        choice = int(input("Pick the position: "))

    print("selected: " + str(choice))
    return choice

# The main program
print('Welcome to Tic Tac Toe!')
player='Player' + str(choose_first())
p1marker , p2marker = player_input(player)

board = [' '] * 9
display_board(board)

game_on = True

while game_on:
    #Player 1 Turn
    position = player_choice(player)
    place_marker(board, p1marker, position)
    winCombo=win_check(board, p1marker)
    display_board(board, winCombo)
    if winCombo != None:
        print(f"Congratulations! {player} won")
        break
    
    
    # Player2's turn.
    position = player_choice(player)
    place_marker(board, p2marker, position)
    winCombo=win_check(board, p2marker)
    display_board(board, winCombo)
    if winCombo != None:
        print(f"Congratulations! {player} won")
        break

