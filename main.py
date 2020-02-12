def connectFour():
	'''makes a game of connect 4'''
	welcomeMessage()
	board = generateBoard()
	playerOneMove = True
	notWin = True
	while notWin:
		board, playerOneMove, notWin = playerMove(playerOneMove,board)
	if not playerOneMove:
		print("Player 1 won! Type connectFour() to play again!")
	else:
		print("Player 2 won! Type connectFour() to play again!")

def welcomeMessage():
	'''Makes a welcome message for the player'''
	print("Welcome to connect four! Play at your own risk! (It might break, we offer no warranty if it breaks!)")

def printBoard(board):
	'''Prints board for connect 4'''
	print("1234567")
	for i in board:
		line = ''.join(i)
		print(line)

def generateBoard():
	'''Makes a new board for connect 4'''
	board = [[],[],[],[],[],[]]
	for i in range(len(board)):
		for j in range(7):
			board[i].append("-")
	printBoard(board)
	return board

def playerMove(playerOneMove, board):
	'''One move in Connect Four'''
	returnStuff = []
	playPiece = "-"
	if playerOneMove:
		playPiece = "X"
	else:
		playPiece = "O"
	columnChosen = int(input(playPiece +", select a column to put your piece in (between 1 and 7, we are not responsible for invalid values): "))
	playingColumn = []
	for i in range(len(board)):
		playingColumn.append(board[i][columnChosen-1])
	playingColumn = playingColumn[::-1]  #reverses the column to easily put the playing piece at the bottom of the column
	playedRow = 0
	for i in range(len(playingColumn)):
		if playingColumn[i] == "-":
			board[5-i][columnChosen-1] = playPiece
			playedRow = 6-i
			break
	printBoard(board)
	returnStuff.append(board)
	returnStuff.append(not playerOneMove)
	returnStuff.append(not didWin(board, playedRow, columnChosen))
	return returnStuff
	
def didWin(board,playedRow, playedColumn):
	'''checks if the player won'''
	winTestArray = []
	winTestArray.append(horizontalWin(board,playedRow,playedColumn))
	winTestArray.append(verticalWin(board,playedRow,playedColumn))
	winTestArray.append(nwSEDiagonalWin(board,playedRow,playedColumn))
	winTestArray.append(swNEDiagonalWin(board,playedRow,playedColumn))
	return True in winTestArray

def horizontalWin(board,playedRow, playedColumn):
	'''sees if you win horizontally'''
	win = False
	horizontalRow = board[playedRow-1]
	horizontalCounter = 1
	for i in range(len(horizontalRow)-1):
		if horizontalCounter != 4:
			if horizontalRow[i] == horizontalRow[i+1] and horizontalRow[i] != '-':
				horizontalCounter+=1
			else:
				horizontalCounter = 1
		if horizontalCounter == 4:
			win = True
			break
	return win

def verticalWin(board,playedRow, playedColumn):
	'''sees if you win vertically'''
	win = False
	verticalColumn = []
	for i in range(len(board)):
		verticalColumn.append(board[i][playedColumn-1])
	verticalCounter = 1
	for i in range(len(verticalColumn)-1):
		if verticalCounter != 4:
			if verticalColumn[i] == verticalColumn[i+1] and verticalColumn[i] != '-':
				verticalCounter+=1
			else:
				verticalCounter= 1
		if verticalCounter == 4:
			win = True
			break
	return win

def nwSEDiagonalWin(board,playedRow, playedColumn):
	'''sees if you win on downward diagonals'''
	win = False
	nwSEDiagonal = [board[playedRow-1][playedColumn-1]]
	for i in range(1,7):
		try:
			rowToAdd=playedRow-1-i
			columnToAdd = playedColumn-1-i
			if rowToAdd < 0 or columnToAdd < 0:
				raise Exception
			nwSEDiagonal.append(board[rowToAdd][columnToAdd])
		except:
			break
	nwSEDiagonal = nwSEDiagonal[::-1]
	for i in range(1,7):
		try:
			rowToAdd = playedRow-1+i
			columnToAdd = playedColumn-1+i
			nwSEDiagonal.append(board[rowToAdd][columnToAdd])
		except:
			break
	nwSEDiagonalCounter = 1
	for i in range(len(nwSEDiagonal)-1):
		if nwSEDiagonalCounter != 4:
			if nwSEDiagonal[i] == nwSEDiagonal[i+1] and nwSEDiagonal[i] != '-':
				nwSEDiagonalCounter+=1
			else:
				nwSEDiagonalCounter= 1
		if nwSEDiagonalCounter == 4:
			win = True
			break
	return win

def swNEDiagonalWin(board,playedRow, playedColumn):
	'''sees if you win on downward diagonals'''
	win = False
	swNEDiagonal = [board[playedRow-1][playedColumn-1]]
	for i in range(1,7):
		try:
			rowToAdd = playedRow - 1 + i
			columnToAdd = playedColumn -1 - i
			if columnToAdd < 0:
				raise Exception
			swNEDiagonal.append(board[rowToAdd][columnToAdd])
		except:
			break
	swNEDiagonal = swNEDiagonal[::-1]
	for i in range(1,7):
		try:
			rowToAdd = playedRow - 1 - i
			columnToAdd = playedColumn -1 + i
			if rowToAdd < 0:
				raise Exception
			swNEDiagonal.append(board[rowToAdd][columnToAdd])
		except:
			break
	swNEDiagonalCounter = 1
	for i in range(len(swNEDiagonal)-1):
		if swNEDiagonalCounter != 4:
			if swNEDiagonal[i] == swNEDiagonal[i+1] and swNEDiagonal[i] != '-':
				swNEDiagonalCounter+=1
			else:
				swNEDiagonalCounter= 1
		if swNEDiagonalCounter == 4:
			win = True
			break
	return win
	
connectFour()