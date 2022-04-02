import numpy as np
import itertools

class PuzzleTuple:

    # INITIATOR FUNCTIONS

    def __init__(self, puzzle, cost, moveMade):
        self.puzzle = puzzle # Puzzle contains a 1D numpy array of 16 elements
        self.cost = cost
        self.moveMade = moveMade
    
    # GETTER FUNCTIONS
    def returnPuzzleBytes(self):
        return self.puzzle.tobytes()
    
    def returnPuzzle(self):
        return self.puzzle
    
    def returnCost(self):
        return self.cost
    
    def returnMoveMade(self):
        return self.moveMade
    
    # SETTER FUNCTIONS

    def setPuzzle(self, puzzle):
        self.puzzle = puzzle
    
    def setCost(self, cost):
        self.cost = cost
    
    def setMoveMade(self, moveMade):
        self.moveMade = moveMade
    
    # COMPARISON FUNCTIONS

    def __eq__(self, other):
        return self.returnPuzzleBytes() == other.returnPuzzleBytes()
    
    def __lt__(self, other):
        return self.returnCost() < other.returnCost()
    
    def isGoal(self):
        return self.returnPuzzleBytes() == np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]).tobytes()

    # VOID FUNCTIONS

    def printPuzzle(self):
        for i in range(16):
            if i % 4 == 0 and i != 0:
                print("\n", end="")
            print(self.puzzle[i], end=" ")
        print()
    
    # COST COUNTER

    def countCost(self):
        cost = 0
        for i in range(16):
            if self.puzzle[i] != i + 1:
                cost += 1
        self.cost = cost
        return cost
    
    def copy(self):
        return PuzzleTuple(self.returnPuzzle(), self.returnCost(), self.returnMoveMade())


def checkIsSolvable(PuzzleTuple):
    totalKurang = 0
    for i in range(len(PuzzleTuple.returnPuzzle())):
        countKurang = 0
        testPuzzle = PuzzleTuple.returnPuzzle()[i]
        if testPuzzle == 16 and i % 2 == 0: # Dibalik, soalnya array starting pointnya 0 dan indeks yang dapet X = 1 itu ganjil di ppt tapi mulai dari 1
            totalKurang += 1
            print("Elemen X memiliki nilai KURANG(i) senilai 1")
        elif testPuzzle == 16 and i % 2 != 0:
            print("Elemen X memiliki nilai KURANG(i) senilai 0")
        for j in range(i + 1, len(PuzzleTuple.puzzle)):
            if PuzzleTuple.puzzle[i] > PuzzleTuple.puzzle[j]:
                countKurang += 1
        print(f'Elemen {testPuzzle} memiliki nilai KURANG(i) senilai {countKurang}')
        totalKurang += countKurang
    if totalKurang % 2 == 0:
        print("Posisi awal puzzle memiliki solusi dengan nilai KURANG(i) sebesar {}".format(totalKurang))
        return True
    else:
        print("Posisi awal puzzle tidak memiliki solusi dengan nilai KURANG(i) sebesar {}".format(totalKurang))
        return False

def whereEmptyBlock(PuzzleTuple):
    for i in range(len(PuzzleTuple.returnPuzzle())):
        if PuzzleTuple.returnPuzzle()[i] == 16:
            return i

def whereToMove(emptyBlockIdx):
    # Urutan prioritas : 'R', 'L', 'U', 'D'
    if (emptyBlockIdx == 0):
        return ['R', 'D']
    elif (emptyBlockIdx == 3):
        return ['L', 'D']
    elif (emptyBlockIdx == 12):
        return ['R', 'U']
    elif (emptyBlockIdx == 15):
        return ['L', 'U']
    elif (emptyBlockIdx == 1 or emptyBlockIdx == 2):
        return ['R', 'L', 'D']
    elif (emptyBlockIdx == 4 or emptyBlockIdx == 8):
        return ['R', 'U', 'D']
    elif (emptyBlockIdx == 7 or emptyBlockIdx == 11):
        return ['L', 'U', 'D']
    elif (emptyBlockIdx == 13 or emptyBlockIdx == 14):
        return ['R', 'L', 'U']
    else:
        return ['R', 'L', 'U', 'D']

def switchLeft(PuzzleTuple, emptyBlockIdx):
    PuzzleTuple.setPuzzle(np.insert(PuzzleTuple.returnPuzzle(), emptyBlockIdx - 1, 16))
    PuzzleTuple.setPuzzle(np.delete(PuzzleTuple.returnPuzzle(), emptyBlockIdx + 1))
    return PuzzleTuple
        
def switchRight(PuzzleTuple, emptyBlockIdx):
    PuzzleTuple.setPuzzle(np.insert(PuzzleTuple.returnPuzzle(), emptyBlockIdx + 2, 16))
    PuzzleTuple.setPuzzle(np.delete(PuzzleTuple.returnPuzzle(), emptyBlockIdx))
    return PuzzleTuple

def switchUp(PuzzleTuple, emptyBlockIdx):
    temp = PuzzleTuple.returnPuzzle()[emptyBlockIdx - 4]
    PuzzleTuple.setPuzzle(np.insert(PuzzleTuple.returnPuzzle(), emptyBlockIdx - 4, 16))
    PuzzleTuple.setPuzzle(np.delete(PuzzleTuple.returnPuzzle(), emptyBlockIdx - 3))
    PuzzleTuple.setPuzzle(np.insert(PuzzleTuple.returnPuzzle(), emptyBlockIdx, temp))
    PuzzleTuple.setPuzzle(np.delete(PuzzleTuple.returnPuzzle(), emptyBlockIdx + 1))
    return PuzzleTuple

def switchDown(PuzzleTuple, emptyBlockIdx):
    temp = PuzzleTuple.returnPuzzle()[emptyBlockIdx + 4]
    PuzzleTuple.setPuzzle(np.insert(PuzzleTuple.returnPuzzle(), emptyBlockIdx + 4, 16))
    PuzzleTuple.setPuzzle(np.delete(PuzzleTuple.returnPuzzle(), emptyBlockIdx + 5))
    PuzzleTuple.setPuzzle(np.insert(PuzzleTuple.returnPuzzle(), emptyBlockIdx, temp))
    PuzzleTuple.setPuzzle(np.delete(PuzzleTuple.returnPuzzle(), emptyBlockIdx + 1))
    return PuzzleTuple

def moveTile(PuzzleTuple, emptyBlockIdx, move):
    if move == 'R':
        PuzzleTuple = switchRight(PuzzleTuple, emptyBlockIdx)
    elif move == 'L':
        PuzzleTuple = switchLeft(PuzzleTuple, emptyBlockIdx)
    elif move == 'U':
        PuzzleTuple = switchUp(PuzzleTuple, emptyBlockIdx)
    elif move == 'D':
        PuzzleTuple = switchDown(PuzzleTuple, emptyBlockIdx)
    return PuzzleTuple

# def costCounter(PuzzleTuple):
#     cost = 0
#     for i in range(len(PuzzleTuple.returnPuzzle())):
#         if PuzzleTuple.returnPuzzle()[i] != i + 1:
#             cost += 1
#     return cost

# def solvePuzzle(PuzzleTuple):
#     if PuzzleTuple.isTheAnswer():
#         return PuzzleTuple
#     else:
#         emptyBlockIdx = whereEmptyBlock(PuzzleTuple)
#         moveList = whereToMove(emptyBlockIdx)
#         for move in moveList:
#             PuzzleTuple = moveTile(PuzzleTuple, emptyBlockIdx, move)
#             if PuzzleTuple.isTheAnswer():
#                 return PuzzleTuple
#             else:
#                 PuzzleTuple = solve(PuzzleTuple)
#                 if PuzzleTuple.isTheAnswer():
#                     return PuzzleTuple
#                 else:
#                     PuzzleTuple = moveTile(PuzzleTuple, emptyBlockIdx, move)
#         PuzzleTuple.printPuzzle()
#         return PuzzleTuple