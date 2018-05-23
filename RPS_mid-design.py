
def computerPlay( handsList ):
	return 'r'
def chooseWinner(userScore, computerScore):
	return 1



# Print an introduction. Mention typing q to quit.

# Get some user input
userIn = input()
# In each round (until the user types q to quit):
while(userIn != 'q'):
	# Generate the computer's move. Make use of some kind of random behavior.
	computerIn = computerPlay( [] )

	# Use some logic to determine who wins.
	winner = chooseWinner(userIn, computerIn)

	print('You chose: ', userIn, '\nComputer chose: ', computerIn)
	# Let the player know who wins.


	# Any long term score keeping needs to happen here if it's happening at all.


	# Get next user input.
	userIn = input()

# After user quits, print some goodbye message.
