#Global Variables

#Holds and keeps track of the board positions
board = ["-", "-","-",
         "-", "-","-",
         "-", "-","-",]

#Keep track of the current player between X and O, X goes first
current_player = "X"

#Who is the winner, default set to none
win = None

#Keeps track of if the game is over
continuing = True

#Keeps track of wins for both players
xWins = 0
oWins = 0
ties = 0

def display_board():
    #Display the board with lines separating them
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2] + "      0 | 1 | 2")
    print(board[3] + " | " + board[4] + " | " + board[5] + "      3 | 4 | 5")
    print(board[6] + " | " + board[7] + " | " + board[8] + "      6 | 7 | 8")
    print("\n")

def play():
    #Need to use global varibles for xWins and oWins
    global xWins
    global oWins
    global ties
    
    #Reset the board
    reset_game()
    
    #Display the board
    display_board()
    
    #While the game can continue (no one has won or tied)
    while continuing:
        #Player makes their move
        make_move(current_player)
        
        #Check to see if a player has won after that turn
        check_win()
        
        #If no player has won, check to see if there is a tie
        check_tie()
        
        #If no one has won or tied, flip the current player
        flip_player()
    
    #After leaving the while loop, there should be a winner or a tie game
    if win == "X":
        print("Player X has won!")
        xWins = xWins + 1
    elif win == "O":
        print("Player O has won!")
        oWins = oWins + 1
    else:
        print("Tie Game!")
        ties = ties + 1

def make_move(player):
    #Display the current player's turn
    print(player + "'s turn")
    
    #Ask the player to input a cell to choose from
    pos = input("Pick a position from 0 - 8: ")
    
    works = False
    while not works:
        #Make sure that the input is valid
        while pos not in ["0", "1", "2", "3", "4", "5", "6", "7", "8"]:
            pos = input("Please pick a position from 0 - 8: ")
        
        pos = int(pos)
        
        #Check to make sure that the spot is not occupied
        if board[pos] == "-":
            works = True
        else:
            print("That spot is occupied. Try again.")
    
    #Mark the position with the player's character
    board[pos] = player
    
    #Display the board with the newly marked cell
    display_board()

    
def flip_player():
    #We need to use the global variable current_player
    global current_player

    #Flip the player based on the current player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"
        
    
def check_win():
    #Need to use global variables continuing and win
    global continuing
    global win
    
    #Check if there is a winner in rows
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"
    
    if row1:
            continuing = False
            win = board[0]
    elif row2:
            continuing = False
            win = board[3]
    elif row3:
            continuing = False
            win = board[6]
    else:
        win = None
    
    #Check if there is a winner in columns
    col1 = board[0] == board[3] == board[6] != "-"
    col2 = board[1] == board[4] == board[7] != "-"
    col3 = board[2] == board[5] == board[8] != "-"

    if col1:
            continuing = False
            win = board[0]
    elif col2:
            continuing = False
            win = board[1]
    elif col3:
            continuing = False
            win = board[2]
    else:
        win = None
    
    #Check if there is a winner in diagonal
    diag1 = board[0] == board[4] == board[8] != "-"
    diag2 = board[2] == board[4] == board[6] != "-"

    if diag1:
            continuing = False
            win = board[0]
    elif diag2:
            continuing = False
            win = board[2]
    else:
        win = None
            

def check_tie():
    #Make use of global variable continuing
    global continuing
    
    #If there are no more "-" spaces, and neither player has won, the game is tied
    if "-" not in board:
        continuing = False
        return True
    else:
        return False

def play_again():
    #Ask if the players want to play again
    print("Do you want to play again? (yes or no)")
    return input().lower().startswith('y')

def reset_game():
    #Make use of global variables to be reset
    global board
    global win
    global continuing
    global current_player

    #Set the values back to the original values
    board = ["-", "-","-",
         "-", "-","-",
         "-", "-","-",]
    win = None
    continuing = True
    current_player = "X"

#Call play() to start the game    
play()

#While the user wants to continue playing continue to play
while play_again():
    play()

#At the end of the game, each player's score is displayed
print("\n")
print("Player X won " + str(xWins) + " times")
print("Player O won " + str(oWins) + " times")
print("Players tied " + str(ties) + " times")
print("Thanks for playing! :)")    
