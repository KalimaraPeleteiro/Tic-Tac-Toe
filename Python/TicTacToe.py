from random import randint

# Setting the game table
game_table = [[[' '], [' '], [' ']] for c in range (0, 3)]


# Just for better understanding
def skip_line() -> str:
    print('')


# Function to show the game table
def show_table(table: list) -> None:
    skip_line()
    for row in range(0, 3):
        for column in range(0, 3):
            print(table[row][column], end='\t')
        skip_line()


# Function to update the table
def update_table(table: list, move: tuple, computer=False) -> list:
    if computer == True:
        table[move[0]][move[1]] = ['O']
    else:
        table[move[0]][move[1]] = ['X']
    
    return table


# Look for any winner
def check_table(table: list) -> bool:
    for row in range(0, 2):
        if table[row][0] == table[row][1] == table[row][2] != [' ']:
            return True
    for column in range(0, 2):
        if table[0][column] == table[1][column] == table[2][column] != [' ']:
            return True
    if table[0][0] == table[1][1] == table[2][2] != [' ']:
        return True
    if table[0][2] == table[1][1] == table[2][0] != [' ']:
        return True
    if table[0][0] != table[0][1] != table[0][2] != table[1][0] != table[1][1] != table[1][2] != table[2][0] != table[2][1] != table[2][2] != [' ']:
        return True
    
    return False


# Function for moves both for player and computer
def move_function(table: list, computer=False) -> None:
    if computer == True:
        while True:
            row_guess = randint(0, 2)
            column_guess = randint(0, 2)

            if table[row_guess][column_guess] == [' ']:
                return row_guess, column_guess
    else:
        while True:
            try:
                player_row_guess = int(input("Which row do you choose (1 - 3)? ")) - 1
                player_column_guess = int(input("Which column do you choose (1 - 3)? ")) - 1
            except ValueError:
                print("Error! Please enter a valid number!\n")
            else:
                if (player_row_guess or player_column_guess) not in (0, 1, 2):
                    print("Error! Please enter a number between 1 and 3!\n")
                    continue
                elif table[player_row_guess][player_column_guess] == [' ']:
                    return player_row_guess, player_column_guess
                else:
                    print("Error! There's already a symbol in that place!")
    

def start_game() -> None:

    global game_table

    print("="*30)
    print("Welcome to the TicTacToe Game!")
    print("\nPlayer - X")
    print("Computer - O")
    print("\nLet's Begin!")
    print("="*30)

    while True:

        show_table(game_table)

        player_guess = move_function(game_table)
        game_table = update_table(game_table, player_guess)

        computer_guess = move_function(game_table, computer=True)
        game_table = update_table(game_table, computer_guess, computer=True)

        game_state = check_table(game_table)
        print("-"*40)

        if game_state == True:

            show_table(game_table)

            print("\nThe game is Over.")
            break



if __name__ == "__main__":
    start_game()