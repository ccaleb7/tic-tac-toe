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

def play():
	display_board()
	
	while continuing:
		make_move(current_player)
		
		check_win()
		
		check_tie()
		
		flip_player()
	
	if win == "X":
		print("Player X has won!")
	elif win == "O":
		print("Player O has won!")
	else:
		print("Tie Game!")

def make_move(player):
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
	
	if current_player == "X":
		current_player = "O"
	else:
		current_player = "X"
		
	
def check_win():
	global continuing


def check_tie():
	#Make use of global variable continuing
	global continuing
	
	#If there are no more "-" spaces, and neither player has won, the game is tied
	if "-" not in board:
		continuing = False
		return True
	else:
		return False
	

play()
