from random import randint #For selecting a random totoro

"""
Initial cell (0,0)
"""


# // DIV
# % MOD
class mazeCell:
	def __init__(self,x,y):
		self.lefWall = True
		self.rigWall = True
		self.topWall = True
		self.botWall = True

		self.x = x
		self.y = y

	def isVisited():
		if (self.lefWall == True) and (self.rigWall == True) and (self.topWall == True) and (self.botWall == True):
			return False
		else:
			return True

class mazeBoard:

	def __init__(self,sizex,sizey):
		
		self.cells = []
		self.sizex = sizex
		self.sizey = sizey
		for cell in range(sizey*sizex):
			x = cell % sizex
			y = cell // sizey
			self.cells.append(mazeCell(x,y))

		self.initialCell = self.cells[0]
	
	def indexOf(self,x,y):
		return x + (y*self.sizey)

	def verify(self,x,y):
		return (self.sizex > x) and (self.sizey > y) and (0<=x) and (0<=y)
	
	def getTotoros(self,cell):
		totoros = []
		x = cell.x
		y = cell.y
		#left
		if(verify(x-1,y)):
			totoros.append(cells[indexOf(x-1,y)])
		#right
		if(verify(x+1,y)):
			totoros.append(cells[indexOf(x+1,y)])
		#top
		if(verify(x,y+1)):
			totoros.append(cells[indexOf(x,y+1)])
		#bottom
		if(verify(x,y-1)):
			totoros.append(cells[indexOf(x,y-1)])

		return totoros

	def getUnvisitedTotoros(self,cell):
		unvisitedTotoros = []

		totoros = getTotoros(cell)
		for totoro in totoros:
			if(not totoro.isVisited()):
				unvisitedTotoros.append(totoro)

		return unvisitedTotoros

	def removeWallBetweenCells(self,cell1,cell2):
		index1 = indexOf(cell1.x,cell1.y)
		index2 = indexOf(cell2.x,cell2.y)



	def recursiveBacktracker():
		numCellsToVisit = self.x * self.y
		cellStack = []
		#http://en.wikipedia.org/wiki/Maze_generation_algorithm#Recursive_backtracker
		#1
		currentCell = self.initialCell
		#2
		while numCellsToVisit > 0:
			unvisited = getUnvisitedTotoros(currentCell)
			#1
			if len(unvisited)>0:
				#1
				randPick = randint(0,len(unvisited))
				#2
				cellStack.append(unvisited[randPick])
				#3
				removeWallBetweenCells(currentCell,unvisited[randPick])
				#4
				currentCell = self.cells[indexOf(unvisited[randPick].x,unvisited[randPick].y)]			#2	
			
			"""
			elif:
				1==1
			#3
			else:
				1==1
			"""

a = mazeBoard(3,3)
