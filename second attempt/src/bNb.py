import numpy as np
import itertools

class PuzzleTuple:

    # INITIATOR FUNCTIONS
    objectsBuilt = itertools.count()

    def __init__(self, puzzle, cost, moveMade, parentID):
        self.puzzle = puzzle # Puzzle contains a 1D numpy array of 16 elements
        self.cost = cost
        self.moveMade = moveMade
        self.parentID = parentID
        self.selfID = next(self.objectsBuilt)
    
    # GETTER FUNCTIONS
    def returnPuzzleBytes(self):
        return self.puzzle.tobytes()
    
    def returnPuzzle(self):
        return self.puzzle
    
    def returnCost(self):
        return self.cost
    
    def returnMoveMade(self):
        return self.moveMade
    
    def returnParentID(self):
        return self.parentID
    
    def returnSelfID(self):
        return self.selfID
    
    # SETTER FUNCTIONS

    def setPuzzle(self, puzzle):
        self.puzzle = puzzle
    
    def setCost(self, cost):
        self.cost = cost
    
    def setMoveMade(self, moveMade):
        self.moveMade = moveMade
    
    def setParentID(self, parentID):
        self.parentID = parentID
    
    # COMPARISON FUNCTIONS

    def __eq__(self, other):
        return self.returnPuzzleBytes() == other.returnPuzzleBytes()
    
    def __lt__(self, other):
        return self.returnCost() < other.returnCost()

    # VOID FUNCTIONS

    def printPuzzle(self):
        for i in range(16):
            if i % 4 == 0 and i != 0:
                print("\n", end="")
            print(self.puzzle[i], end=" ")
    
