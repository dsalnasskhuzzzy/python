class board:
	def __init__(self,demensions,playerCount):
		#Both Player Count and Demensions must be natural numbers
		self.demensions = demensions

		self.marks = [[] for x in range(playerCount)]

	def addMarkForPlayer(self,mark,playerID):
		self.marks[playerID].append(mark)

	def checkIfValidMark(self,mark):
		if(len(mark)!=self.demensions):
			return False
		for part in mark:
			if(part != 0 and part != 1 and part != 2):
				return False
		for playerMarks in self.marks:
			for otherMark in playerMarks:
				if(otherMark == mark):
					return False

		#If it's not found to be a bad mark, it's Valid
		return True

	def lazyWinCheck(self,playerID):
		#Only checks the to see if the players last move has won them the game
		playerMarks = self.marks[playerID]
		moveCount = len(playerMarks)
		lastMark = playerMarks[moveCount-1]
		for index in range(moveCount-1):
			for secondIndex in range(index+1,moveCount-1):
				if(self.checkWinCoords(lastMark,playerMarks[index],playerMarks[secondIndex])):
					return True
		#If no valid win condition has been found the player has not won
		return False

	def checkWinCoords(self,c1,c2,c3):
		ascendingFound = False
		for index in range(self.demensions):
			a = c1[index]
			b = c2[index]
			c = c3[index]
			ascending = (a!=b and b!=c and c!=a) and (a+b+c == 3)
			equality = a==b and b==c
			if (not ascendingFound) and (ascending):
				ascendingFound = True
			#Check for ascending then check for equality
			if not (ascending or equality):
				return False
		#If we make it to the end of this check and there is an ascending then it is a valid win condition
		if ascendingFound:
			return True

plNum = 2
dem = 2
game = board(dem,plNum)
gameDone = False

playerID = -1
while(not gameDone):
	playerID = (playerID + 1) % plNum
	mark = []
	while mark==[]:
		for x in range(dem):
			input = int(raw_input("PLAYER %d Enter (0,1, or 2) for demension %d |" % (playerID,x)))
			mark.append(input)
			print mark
		if not game.checkIfValidMark(mark):
			print "Invalid Mark Thrown Away"
			mark = []
	print "Mark Completed"
	game.addMarkForPlayer(mark,playerID)
	gameDone = game.lazyWinCheck(playerID)
print "%d has won" % (playerID)