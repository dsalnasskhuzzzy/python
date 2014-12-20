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

		self.isVisited = False

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
		if(self.verify(x-1,y)):
			totoros.append(self.cells[self.indexOf(x-1,y)])
		#right
		if(self.verify(x+1,y)):
			totoros.append(self.cells[self.indexOf(x+1,y)])
		#top
		if(self.verify(x,y+1)):
			totoros.append(self.cells[self.indexOf(x,y+1)])
		#bottom
		if(self.verify(x,y-1)):
			totoros.append(self.cells[self.indexOf(x,y-1)])

		return totoros

	def getUnvisitedTotoros(self,cell):
		unvisitedTotoros = []

		totoros = self.getTotoros(cell)
		for totoro in totoros:
			if(not totoro.isVisited):
				unvisitedTotoros.append(totoro)

		return unvisitedTotoros

	def removeWallBetweenCells(self,cell1,cell2):
		index1 = self.indexOf(cell1.x,cell1.y)
		index2 = self.indexOf(cell2.x,cell2.y)
		if self.cells[index1].x > self.cells[index2].x:
			#Cell1 is to the Right of Cell2
			self.cells[index1].lefWall = False
			self.cells[index2].rigWall = False
		elif self.cells[index1].x < self.cells[index2].x:
			#Cell1 is to the Left of Cell2
			self.cells[index1].rigWall = False
			self.cells[index2].lefWall = False
		elif self.cells[index1].y > self.cells[index2].y:
			#Cell1 is Above Cell2
			self.cells[index1].botWall = False
			self.cells[index2].topWall = False
		else: #self.cells[index1].y > self.cells[index2].y:
			#Cell1 is Below Cell2
			self.cells[index1].topWall = False
			self.cells[index2].botWall = False



	def recursiveBacktracker(self):
		numCellsToVisit = self.sizex * self.sizey
		cellStack = []
		#http://en.wikipedia.org/wiki/Maze_generation_algorithm#Recursive_backtracker
		#1
		currentCell = self.initialCell
		#2
		while numCellsToVisit > 0:
			unvisited = self.getUnvisitedTotoros(currentCell)
			#1
			if len(unvisited)>0:
				#1
				randPick = randint(0,len(unvisited)-1)
				#2
				cellStack.append(unvisited[randPick])
				#3
				self.removeWallBetweenCells(currentCell,unvisited[randPick])
				#4
				currentCell = self.cells[self.indexOf(unvisited[randPick].x,unvisited[randPick].y)]			
				self.cells[self.indexOf(unvisited[randPick].x,unvisited[randPick].y)].isVisited = True
				numCellsToVisit = numCellsToVisit - 1
			#2	
			elif len(cellStack)!=0:
				#1
				#2
				currentCell = cellStack.pop()
			#3
			else:
				pickFrom = []
				for x in self.cells:
					if (not x.isVisited):
						pickFrom.append(x)
				randPick = randint(0,len(pickFrom)-1)		
				currentCell = self.cells[self.indexOf(pickFrom[randPick].x,pickFrom[randPick].y)]
				numCellsToVisit = numCellsToVisit - 1

	def debugPrint(self):
		for x in self.cells:
			print x.topWall
			print x.rigWall

a = mazeBoard(3,3)
a.recursiveBacktracker()

test = a.cells
for t in test:
	print "r:%s l:%s t:%s b:%s" % (t.rigWall,t.lefWall,t.topWall,t.botWall)
