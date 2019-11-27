board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

def check(ls=board):
	if ls[0]==ls[1]==ls[2]!=' ' or ls[3]==ls[4]==ls[5]!=' ' or ls[6]==ls[7]==ls[8]!=' ':
		return True;
	elif ls[0]==ls[3]==ls[6]!=' ' or ls[1]==ls[4]==ls[7]!=' ' or ls[2]==ls[5]==ls[8]!=' ':
		return True
	elif ls[0]==ls[4]==ls[8]!=' ' or ls[2]==ls[4]==ls[6]!=' ':
		return True
	else:
		return False

move_of_X = True
win = None

player1 = input("Player I Name: ")
player2 = input("Player II Name: ")

player = [player1, player2]
char = ["X", "O"]

def clear_output():
	print("\n"*99)

def drawBoard():
	clear_output()
	for i in range(0,3):
		for j in range(0, 3):
			print(board[(2-i)*3+j], end='')
			if j!=2: print('|', end='')
		if i!=2: print("\n-----")
		else: print("")

for _ in range(1, 10):
	move = input(f"{player[int(not move_of_X)]}'s Move: ")
	
	while board[int(move)-1]!=' ':
		move = input(f"Invalid Move, Try again\n{player[int(not move_of_X)]}'s Move: ")
	move_of_X = not move_of_X
	board[int(move)-1] = char[move_of_X]

	drawBoard()

	if check()==True:
		win = player[move_of_X]
		print(f"{win} won the game...")
		break
	elif _ == 9:
		print("No winner!")