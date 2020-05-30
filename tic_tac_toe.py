from math import inf
from random import choice

board = [[0,0,0],
		[0,0,0],
		[0,0,0]]

PLAYER = -1
AI = 1
AI_PIECE = 'X'
PLAYER_PIECE = 'O'

#########################################################################
#########################################################################

def get_score(board):
	'''
	params:
	board -> the board to get the score if win or lose
	output:
	score -> the score for winning,losing or draw
	'''
	if wins(board,AI):
		score = 1
	elif wins(board,PLAYER):
		score = -1
	else:
		score = 0
	return score

#########################################################################
#########################################################################

def wins(board,player):
	'''
	params:
	board -> the current board
	player -> the player (AI or HUMAN) to check for winning
	output:
	True -> if the player (AI or HUMAN) wins
	False -> if win state is not achieved
	'''
	win_state = [[board[0][0],board[0][1],board[0][2]],
				[board[1][0],board[1][1],board[1][2]],
				[board[2][0],board[2][1],board[2][2]],
				[board[0][0],board[1][0],board[2][0]],
				[board[0][1],board[1][1],board[2][1]],
				[board[0][2],board[1][2],board[2][2]],
				[board[0][0],board[1][1],board[2][2]],
				[board[0][2],board[1][1],board[2][0]],]

	if [player,player,player] in win_state:
		return True
	else:
		return False
###################################################################################
###################################################################################


def game_over(board):
	'''
	function to return True if game is over, i.e. AI wins or PLAYER wins or is a draw
	'''
	return wins(board,AI) or wins(board, PLAYER) or len(empty_cells(board)) == 0

######################################################################################
######################################################################################

def empty_cells(board):
	'''
	takes in input the board and returns the number of available spots for the PLAYER or AI
	'''
	cells = []
	for x,row in enumerate(board):
		for y,cell in enumerate(row):
			if cell == 0:
				cells.append((x,y))
	return cells

#######################################################################################
#######################################################################################

def isValid(x,y):
	'''
	params:
	x -> the row of the board
	y -> the column of the board
	output:
	True -> if the position given is a valid position 
	False -> if the position given is not a valid position
	'''
	if (x,y) in empty_cells(board):
		return True
	else:
		return False

##########################################################################################
##########################################################################################

def put_piece(x,y,player):
	'''
	params:
	x -> the row of the board
	y -> the column of the board
	player -> the player (AI or HUMAN) piece to be placed at the position (x,y)
	output:
	sets the piece of player (AI or HUMAN) at the specified position (x,y)
	'''
	if isValid(x,y):
		board[x][y] == player
		return True
	else:
		return False

############################################################################################
############################################################################################

def minimax(board,depth,player):
	'''
	The main function to determin the score and best position of the board given the state of the board
	params:
	baord -> the current state of the board
	depth -> the depth of the search for the algorithm
			 Searches for the best position down the tree and returns the best position found till
			 depth
	player -> the current player (AI or HUMAN)
	output:
	best -> a list of position (x,y) and the best score from the given state = [x,y,score]
	'''
	if player == AI:
		best = [-1,-1,-inf]
	else:
		best = [-1,-1,inf]

	if depth == 0 or game_over(board):
		score = get_score(board)
		return [-1,-1,score]

	for cell in empty_cells(board):
		x,y = cell[0],cell[1]
		board[x][y] = player
		score = minimax(board,depth-1,-player)
		board[x][y] = 0
		score[0],score[1] = x,y

		if player == AI:
			if score[2] > best[2]:
				best = score

		else:
			if score[2] < best[2]:
				best = score

	return best

######################################################################################
######################################################################################

def draw_board(board):
	'''
	params:
	board -> the current state of the board
	output:
	prints the board with correct piece of the player (AI or HUMAN)
	'''
	for x,row in enumerate(board):
		for y,cell in enumerate(row):
			if (y+1)%3 != 0:
				if cell == AI:
					print(f'{AI_PIECE} | ',end='')
				elif cell == PLAYER:
					print(f'{PLAYER_PIECE} | ',end ='')
				else:
					print(f'{cell} | ',end='')
			elif (y+1)%3 == 0:
				if cell == AI:
					print(f'{AI_PIECE}')
				elif cell == PLAYER:
					print(f'{PLAYER_PIECE}')
				else:
					print(f'{cell}')
		if (x+1)%3 != 0: 
			print('----------')

###########################################################################################
###########################################################################################

def play(board):
	'''
	the main function which starts the game and displays the winner and all
	'''
	draw_board(board)
	print()
	turn = choice([1,2])     # random assignment of the player (AI or HUMAN)
	while len(empty_cells(board))>0 and not game_over(board):	
		if turn %2 == 0:
			player_turn(board)
			turn += 1
		else:
			ai_turn(board)
			turn += 1
	if wins(board,AI): 						#if AI wins
		print()
		print('AI wins!!!')
	elif wins(board,PLAYER): 				#if PLAYER wins
		print()
		print('Player wins!!!')
	else: 									#if draw
		print()
		print('Draw!!!')

##################################################################################################
##################################################################################################

def player_turn(board):
	'''
	takes in valid choice from the player and places it onto board
	'''
	choices = {1:(0,0), 2:(0,1), 3:(0,2),
				4:(1,0), 5:(1,1), 6:(1,2),
				7:(2,0), 8:(2,1), 9:(2,2)}			#mapping of the choice to positions of board

	choice = int(input('\nenter your choice (1-9): '))
	if choice in choices: 									# if position is a valid position between (1-9)
		if choices[choice] in empty_cells(board):			# if position is empty
			board[choices[choice][0]][choices[choice][1]] = PLAYER
		else:												# if position is already taken
			print('\nThe cell is already taken..... Please enter another valid position')
			human_turn(board)
	else:													# if invalid position, i.e. not between (1-9)
		print('\nThe entered choice is not valid..... Please enter a valid number between (1-9)')
		human_turn(board)
	draw_board(board)
	print()

###################################################################################################
###################################################################################################

def ai_turn(board):
	'''
	makes the choice for the AI
	'''
	choicex,choicey,_ = minimax(board,len(empty_cells(board)),AI)
	board[choicex][choicey] = AI
	draw_board(board)
	print()

######################################################################################################
######################################################################################################

play(board)
