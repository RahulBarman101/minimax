from math import inf
from random import choice

board = [[0,0,0],
		[0,0,0],
		[0,0,0]]

PLAYER = -1
AI = 1
AI_PIECE = 'X'
PLAYER_PIECE = 'O'

def get_score(board):
	if wins(board,AI):
		score = 1
	elif wins(board,PLAYER):
		score = -1
	else:
		score = 0
	return score

def wins(board,player):
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

def game_over(board):
	return wins(board,AI) or wins(board, PLAYER)

def empty_cells(board):
	cells = []
	for x,row in enumerate(board):
		for y,cell in enumerate(row):
			if cell == 0:
				cells.append((x,y))
	return cells

def isValid(x,y):
	if (x,y) in empty_cells(board):
		return True
	else:
		return False

def put_piece(x,y,player):
	if isValid(x,y):
		board[x][y] == player
		return True
	else:
		return False

def minimax(board,depth,player):
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

def draw_board(board):
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

def play(board):
	done = False
	draw_board(board)
	print()
	turn = 0
	choices = {1:[0,0],2:[0,1],3:[0,2],4:[1,0],5:[1,1],6:[1,2],7:[2,0],8:[2,1],9:[2,2]}
	while len(empty_cells(board))>0 and not game_over(board):
		
		if turn %2 == 0:
			choice = int(input('enter your choice: '))
			board[choices[choice][0]][choices[choice][1]] = PLAYER
			draw_board(board)
			print()
			turn += 1
		else:
			choicex,choicey,_ = minimax(board,len(empty_cells(board)),AI)
			board[choicex][choicey] = AI
			draw_board(board)
			print()
			turn += 1
	if wins(board,AI):
		print()
		print('AI wins!!!')
	elif wins(board,PLAYER):
		print()
		print('Player wins!!!')
	else:
		print()
		print('Draw!!!')

play(board)

