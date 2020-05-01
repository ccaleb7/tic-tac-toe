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
	
play()
