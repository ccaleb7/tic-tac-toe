# tic-tac-toe
Unix final project
Name: Caleb Choi

This Python project is a game of tic-tac-toe to be played between two players on the command line. It keeps 
track of both player's score and allows the players to play continuously until they choose to end. Players 
are split into "X" and "O" where player "X" always goes first. In terms of winning the game, a player must
match three of it's marker across a row, column, or diagonal. 

To run the project, I ran the main.py file in Python shell where I used the "Run -> Run Module" to test and
play my code. While the program is running, it will provide instructions for the players as well as indicate
which player should be inputing their move. If a player inputs an invalid position, not in 0 - 8, the program
will indicate as so and request the player to input a new value. After every player's move the program checks
to see if any player has won, if so, the game ends and the winning player is shown. If no player has won by 
the time the board is "full" the game is tied and shows that the players have tied. At the end of a player
winning or a tied game, the players are able to play the game again by entering "yes". If they type "no" or
anything that does not start with a 'y', then the game ends and the scores are shown. 
