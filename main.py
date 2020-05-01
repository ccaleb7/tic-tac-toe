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

def display_board():
	print("\n")
	print(board[0] + " | " + board[1] + " | " + board[2])
	print(board[3] + " | " + board[4] + " | " + board[5])
	print(board[6] + " | " + board[7] + " | " + board[8])
	print("\n")
	