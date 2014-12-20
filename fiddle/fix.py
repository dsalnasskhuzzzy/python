"""
Game of Life
0 Dead
1 Alive
"""

width = 5
height = 5

#Define init cells here
AliveCells = [[1,1],[1,2],[1,3]]
maxGen = 5

#2d Array of zeros
def emptyField():
	return [[0 for x in range(width)] for x in range(height)]

def applyAlive(cellSet):
	returnField = emptyField()
	for cell in cellSet:
		returnField[cell[0]][cell[1]] = 1
	return returnField

def printBoard(board):
	for x in board:
		print x

def nextGenAliveCells(cellSet,board):
	deadCellsToCheck = []
	aliveCellsToCheck = cellSet

	nextGeneration = []

	for cell in cellSet:
		for i in range(-1,2):
			for j in range(-1,2):
				if ((i!=0) or (j!=0)) and (cell[0]+i>=0 and cell[0]+i<width) and (cell[1]+j>=0 and cell[1]+j<height):
					if (not([cell[0]+i,cell[1]+j] in aliveCellsToCheck)) and (not([cell[0]+i,cell[1]+j] in deadCellsToCheck)):
						deadCellsToCheck.append([cell[0]+i,cell[1]+j])
		
	for liveCell in aliveCellsToCheck:
		totoro = totoroNum(liveCell,board)
		if totoro == 2 or totoro == 3:
			nextGeneration.append(liveCell)

	for deadCell in deadCellsToCheck:
		totoro = totoroNum(deadCell,board)
		if totoro == 3:
			nextGeneration.append(deadCell)
	return nextGeneration

def totoroNum(cell,board):
	num = 0
	for i in range(-1,2):
		for j in range(-1,2):
			if ((i!=0) or (j!=0)) and (cell[0]+i>=0 and cell[0]+i<width) and (cell[1]+j>=0 and cell[1]+j<height):
				if board[cell[0]+i][cell[1]+j] == 1:
					num+=1
	return num

def tick(info):
	info[1] = nextGenAliveCells(info[1],info[0])
	info[0] = applyAlive(info[1])
	printBoard(info[0])
	return info

#Initialize Stuff	
field = applyAlive(AliveCells)
init = [field,AliveCells]
printBoard(field)

for x in range(1,maxGen):
	print "Generation %d" % (x)
	init = tick(init)




