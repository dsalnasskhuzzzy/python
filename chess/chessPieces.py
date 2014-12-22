class Piece(object):
    def __init__(self,initialPosition):
    	self.position = initialPosition

    def getPosition(self):
    	return self.position

    def setPosition(self,newPosition):
    	self.position = newPosition

	def isValidMove(self,targetPosition,allyPieces,foePieces):
		raise NotImplementedError()

class Pawn(Piece):

class Knight(Piece):

class Bishop(Piece):

class Rook(Piece):

class Pawn(Queen):
