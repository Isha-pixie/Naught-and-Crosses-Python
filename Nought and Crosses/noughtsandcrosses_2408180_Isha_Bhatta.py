'''Name: Isha Bhatta
   Student ID:2408180'''

# Imports the random module for generating random numbers.
import random
# Imports the os.path module for manipulating file paths.
import os.path
# Imports the json module for working with JSON data.
import json
# Initializes the random number generator with a seed value.
random.seed()



def draw_board(board):
    """Draws the Noughts and Crosses board."""
    print(" ", end="")
    print("-" * 11)
    for row in board:
        print("| ", end="")
        print(" | ".join(row), end="")
        print(" |")
        print(" ", end="")
        print("-" * 11)
        

    

def welcome(board):
    """Prints the welcome message,displays the draw board and provides short instructions for the game.\n"""
    print("\nWelcome to the 'Unbeatable Noughts and Crosses' game!\nƪ(˘⌣˘)ʃ \n")
    print("The layout of the board is shown below:\n")
    draw_board(board)
    print("\nInstructions:\n1)The game is played on a 3x3 grid.\n2)Players take turns to place their mark ('X' for the player, 'O' for the computer) in an empty cell.\n3)To make a move, the player enters the number corresponding to the desired cell (1 to 9).\n4)The game ends when the board is full and score is counted.")



def initialise_board(board):
    """Sets all elements of the board to one space ' '."""
    for r in range(3):
        for c in range(3):
            board[r][c] = ' '
    return board

def get_player_move(board):
    """Prompts the user for the cell to put 'X' in
       returns: row and col."""
    while True:
        try:
            move = int(input("\nChoose your square:\n -----------\n| 1 | 2 | 3 |\n -----------\n| 4 | 5 | 6 |\n -----------\n| 7 | 8 | 9 |\n -----------: "))
            if (1 <= move <= 9):
                row =(move- 1)//3
                col =(move- 1)%3
                if board[row][col] == ' ':
                    return row, col
                print("Cell already occupied.")
            else:
                print("Invalid input. Enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Enter a number between 1 and 9.")



def choose_computer_move(board):
    """Randomly selects a cell for the computer to place 'O' and returns the row and column."""
    while True:
        move= random.randint(1, 9)
        row= (move- 1)// 3
        col= (move- 1)% 3
        if board[row][col] == ' ':
            return row, col

        
def check_for_win(board, mark):
    """Checks if the specified player or computer has won the game.
    returns: True if someone won otherwise False"""
    win_lines = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]

    for line in win_lines:
        if all(board[r][c] == mark for r, c in line):
            return True
    return False


def check_for_draw(board):
    
    """Checks if all cells are occupied
       returns: True if they are occupied,otherwise False."""
    if all(cell != ' ' for row in board for cell in row):
        return true

def play_game(board):
    """
    Manages the Noughts and Crosses game.
    Returns:
        1 if the user wins,
        -1 if the computer wins,
        0 if it's a draw.
    """
    initialise_board(board)
    draw_board(board)
    while True:
        row, col = get_player_move(board)
        board[row][col] = 'X'
        draw_board(board)

        if check_for_win(board, 'X'):
            print("You win!\nYou get 1 point")
            return 1
        if check_for_draw(board):
            print("It's a Draw! Try Again!\nYou get 0 points")
            return 0

        print("\nComputer's move: ")
        row, col = choose_computer_move(board)
        board[row][col] = 'O'
        draw_board(board)

        if check_for_win(board, 'O'):
            print("You lose!\n1 point will be deducted from your score in leaderboard")
            return -1
        if check_for_draw(board):
            print("It's a Draw! Try Again!\nYou get 0 point")
            return 0

                
def menu():
    """Displays the menu options and prompts user to choose one of the options."""
    print("\nEnter one of the following options: ")
    print(" 1 - Play the game")
    print(" 2 - Save score in file 'leaderboard.txt'")
    print(" 3 - Load and display the scores from 'leaderboard.txt'")
    print(" q - End the program")
    choice = input("1, 2, 3, or q? ")
    print()
    return choice



def load_scores():
    """Loads the leaderboard scores from the file 'leaderboard.txt' and 
    returns them as a dictionary."""
    leaders = {}
    try:
        if os.path.exists('leaderboard.txt'):
            with open('leaderboard.txt', 'r',) as file:
                leaders = json.load(file)
        else:
            print("Leaderboard file not found.")
    except json.JSONDecodeError:
        print("Error decoding JSON. Leaderboard file may be corrupted.")
    except FileNotFoundError:
        print("File 'leaderboard.txt' not found.")

    return leaders

def save_score(score):
    """Asks the player for their name and saves the current score to the file 'leaderboard.txt'."""
    name = input("Enter your name: ")
    leaders = load_scores()
    

    if not name.isalpha() or not str(score).isdigit():
        print("Invalid input. Please enter a valid name and score.")
        return

    if name in leaders:
        leaders[name] += score
    else:
        leaders[name] = score

    try:
        with open('leaderboard.txt', 'w') as file:
            json.dump(leaders, file)
        print("Score saved successfully.")
    except FileNotFoundError:
        print("Leaderboard file not found.")
    except json.JSONDecodeError as json_error:
        print(f"Error decoding JSON: {json_error}. Leaderboard file may be corrupted.")


def display_leaderboard(leaders):
    """Displays the leaderboard scores."""
    print("Leaderboard:")
    if not leaders:
        print("No scores available.")
    else:
        for name, score in leaders.items():
            print(f"{name}: {score}")


