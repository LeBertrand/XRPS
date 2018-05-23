# Include some code that knows how to choose randomly.
import random

# define list of options
handBeats = {'r':'s', 'p':'r', 's':'p'}
hands = list(handBeats.keys())

intro = 'Welcome to Rock, Paper, Scissors. Type q at any time to quit.'
roundInstr = 'Type r, p or s to play a round of Rock, Paper, Scissors.\nrps> '

# Define procedure for letting computer choose one play from a list of options.
def computerPlay(moveChoices):
	# moveChoices is the list of choices to for computer to choose from.

	computerHand = random.choice(moveChoices) 

	# Whoever asked for the computer's play can move one now, using the following value:
	return computerHand
	print('This line will never print. After "return", we leave the function')

'''Define procedure for choosing winner based on two inputs, assuming first
input is player's choice and second input is computer's. Return 1 for player wins,
0 for tie, -1 for computer wins.'''
def chooseWinner(playerChoice, computerChoice):

	if( playerChoice not in hands ):
		# invalid choice -- return error code -2
		return -2

	if(playerChoice == computerChoice):
		return 0
	# If we reach this line, choices don't match. We would have hit 'return'
	# last line if they did match.
	if( handBeats[playerChoice] == computerChoice ):
		return 1


	# The only way to reach this is if player doesn't win and doesn't tie.
	return -1

def showPrompt(prompt):
	print(prompt)

	# No return statement is necessary. Nothing will come back when this function is called.

def showStandings(playerScore, ComputerScore):
	print('You\'re ', playerScore, ' for ', playerScore + ComputerScore, '.')

################################
#		Actual gameplay        #
################################

showPrompt(intro)
userIn = input(roundInstr)
playerWins = 0
computerWins = 0
# Main loop. All gameplay goes in here.
while(userIn not in ['q', 'Q', 'quit', 'Quit']):

	computerIn = computerPlay( hands )

	winner = chooseWinner(userIn, computerIn) # I put the arguments in the right order.
	'''winner is just a variable holding 1, 0 or -1. Meaningless unless you read
	the comment in chooseWinner function.'''

	print('You chose: ', userIn, '\nComputer chose: ', computerIn)

	if(winner == 1):
		print('You win')
		playerWins += 1
	elif(winner == -1):
		print('You lose')
		computerWins += 1
	elif(winner == 0):
		print('You tie. Let\'s not count that one')
	else:
		print('Maybe you misunderstood the choices')

	showStandings(ComputerScore=computerWins, playerScore=playerWins)
	'''I input the arguments out of order, but explained which is which.'''

	print('') # Space out the rounds for nicer look.

	userIn = input(roundInstr)

# Now back outside the loop.
print('Thanks for playing.')
showStandings(ComputerScore=computerWins, playerScore=playerWins)
