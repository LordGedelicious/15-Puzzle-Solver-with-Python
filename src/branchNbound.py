from asyncio.windows_events import NULL
import json
import numpy as np
import copy
import itertools


class PCMTuple: # PCMTuple = Puzzle Cost Move Tuple

    count = itertools.count()

    def __init__(self, puzzle, cost, moveMade, parentID):
        # Puzzle adalah matrix numpy 4x4
        # Cost adalah cost dari puzzle tersebut (bukan nilai RETURN(i))
        # Awalnya nilai cost adalah 0
        # By default parent ID dari root adalah 0, pembuatan root baru akan memiliki parentID sesuai dengan selfID parentnya
        self.puzzle = puzzle
        self.cost = cost
        self.moveMade = moveMade
        self.selfID = next(self.count)
        self.parentID = parentID
    
    def myPuzzle(self):
        return self.puzzle
    
    def myCost(self):
        return self.cost
    
    def myMoveMade(self):
        return self.moveMade
    
    def mySelfID(self):
        return self.selfID
    
    def myParentID(self):
        return self.parentID
    
    def setPuzzle(self, newPuzzle):
        self.puzzle = newPuzzle
    
    def setCost(self, newCost):
        self.cost = newCost
    
    def setMoveMade(self, newMoveMade):
        self.moveMade = newMoveMade


def printMatrix(PCMTuple):
    matrix = PCMTuple.myPuzzle()
    for i in range(4):
        for j in range(4):
            print(matrix[i][j], end=" ")
        print()

def printPCMTupleDetails(PCMTuple):
    print("Puzzle : ")
    printMatrix(PCMTuple)
    print("Cost : ", PCMTuple.myCost())
    print("Move : ", PCMTuple.myMoveMade())
    print("Parent ID : ", PCMTuple.myParentID())
    print("Self ID : ", PCMTuple.mySelfID())
    print()

def printListPuzzleTuple(listPuzzleTuple):
    for i in range(len(listPuzzleTuple)):
        printPCMTupleDetails(listPuzzleTuple[i])

def measureInitScore(PCMTuple):
    puzzle = PCMTuple.myPuzzle()
    count = 0
    index = 1
    while (index <= 16):
        col = index - 1
        row = index // 4
        if (index > 4):
            col = (index % 4) - 1
        if (index in [4,8,12,16]):
            row -= 1
        if (puzzle[row][col] == 16) and ((row + col) % 2 != 0):
            count += 1
        currentValue = puzzle[row][col]
        # Menggunakan urutan 1 sampai 16
        for i in range(0, 4):
            for j in range(0, 4):
                indexProcessed = i * 4 + (j + 1)
                if (indexProcessed > index and puzzle[i][j] < currentValue):
                    count += 1
        index += 1
    return count

def isSolvable(PCMTuple):
    initial_score = measureInitScore(PCMTuple)
    if (initial_score % 2 == 0):
        print("Solvable with a score of " + str(initial_score))
        return True
    else:
        print("Not solvable with a score of " + str(initial_score))
        return False

def costAliveNodes(puzzle, moveMade):
    cost = moveMade
    for i in range(0, 4):
        for j in range(0,4):
            if (puzzle[i][j] != 16) and (puzzle[i][j] != (i*4 + j + 1)):
                cost += 1
    return cost

def whereIsEmptyBlock(PCMTuple):
    matrix = PCMTuple.myPuzzle()
    for i in range(0, 4):
        for j in range(0, 4):
            if (matrix[i][j] == 16):
                return i, j

def whereCanTileMove(row, col):
    if (row == 0 and col == 0):
        return ['RIGHT', 'DOWN']
    elif (row == 3 and col == 0):
        return ['RIGHT', 'UP']
    elif (row == 0 and col == 3):
        return ['LEFT', 'DOWN']
    elif (row == 3 and col == 3):
        return ['LEFT', 'UP']
    elif (row == 0 and col != 0 and col != 3):
        return ['RIGHT', 'DOWN', 'LEFT']
    elif (row == 3 and col != 0 and col != 3):
        return ['RIGHT', 'LEFT', 'UP']
    elif (col == 0 and row != 0 and row != 3):
        return ['RIGHT', 'DOWN', 'UP']
    elif (col == 3 and row != 0 and row != 3):
        return ['DOWN', 'LEFT', 'UP']
    else:
        return ['RIGHT', 'DOWN', 'LEFT', 'UP']
        
def switchTwoValuesInMatrix(puzzle, rowOne, colOne, rowTwo, colTwo):
    # Switch 2 values di puzzle
    temp = puzzle[rowOne][colOne]
    puzzle[rowOne][colOne] = puzzle[rowTwo][colTwo]
    puzzle[rowTwo][colTwo] = temp
    return puzzle

def sortListPCMTuple(listPCMTuple):
    # Menggunakan selection sort
    for i in range(len(listPCMTuple)):
        minimum = i
        for j in range(i, len(listPCMTuple)):
            if (listPCMTuple[j].myCost() < listPCMTuple[minimum].myCost()):
                minimum = j
        temp = listPCMTuple[i]
        listPCMTuple[i] = listPCMTuple[minimum]
        listPCMTuple[minimum] = temp
    # for i in range(len(listPCMTuple)):
    #     minimum = i
    #     for j in range(i, len(listPCMTuple)):
    #         if (listPCMTuple[j].myCost() == listPCMTuple[minimum].myCost()) and (listPCMTuple[j].myCost() - listPCMTuple[j].myMoveMade() < listPCMTuple[minimum].myCost()- listPCMTuple[j].myMoveMade()):
    #             minimum = j
    #     temp = listPCMTuple[i]
    #     listPCMTuple[i] = listPCMTuple[minimum]
    #     listPCMTuple[minimum] = temp
    return listPCMTuple

def anyHasReachTarget(listPCMTuple):
    for i in range(len(listPCMTuple)):
        countCorrect = 0
        nowTestingPuzzle = listPCMTuple[i].myPuzzle()
        for j in range(0, 4):
            for k in range(0, 4):
                if (nowTestingPuzzle[j][k] == (j*4 + k + 1)):
                    countCorrect += 1
        if (countCorrect == 16):
            return True
    return False

def moveTiles(firstPCMTuple, listPCMTuple, visitedPCMTuple):
    # Dibagi jadi dua kondisi
    # Pertama, kalau untuk inisiasi pertama kali, dia diurutkan berdasarkan cost
    # Kedua, kalau udah move >= 1, simpul dengan cost terendah selanjutnya bakal dimajuin ke depan queue, sisanya ke belakang
    tempListPCMTuple = []
    if (len(listPCMTuple) == 0):
        baselinePCMTuple = firstPCMTuple
        baselinePuzzle = baselinePCMTuple.myPuzzle()
        countMoveMade = baselinePCMTuple.myMoveMade()
    else:
        baselinePCMTuple = listPCMTuple.pop(0)
        baselinePuzzle = baselinePCMTuple.myPuzzle()
        countMoveMade = baselinePCMTuple.myMoveMade()
    # print(len(listPCMTuple))
    # Buat dulu semua kemungkinan puzzle yang bisa dibuat
    row, col = whereIsEmptyBlock(baselinePCMTuple)
    possibleMoves = whereCanTileMove(row, col)
    for move in possibleMoves:
        indexPuzzle = json.loads(json.dumps(baselinePuzzle))
        if (move == 'RIGHT'):
            newPuzzle = switchTwoValuesInMatrix(indexPuzzle, row, col, row, col + 1)
        elif (move == 'DOWN'):
            newPuzzle = switchTwoValuesInMatrix(indexPuzzle, row, col, row + 1, col)
        elif (move == 'LEFT'):
            newPuzzle = switchTwoValuesInMatrix(indexPuzzle, row, col, row, col - 1)
        elif (move == 'UP'):
            newPuzzle = switchTwoValuesInMatrix(indexPuzzle, row, col, row - 1, col)
        newPuzzleTuple = PCMTuple(newPuzzle, baselinePCMTuple.myCost(), countMoveMade+1, baselinePCMTuple.mySelfID())
        if (newPuzzleTuple not in visitedPCMTuple):
            newPuzzleTuple.setCost(costAliveNodes(newPuzzle, countMoveMade + 1))
            newPuzzleTuple.setPuzzle(newPuzzle)
            tempListPCMTuple.append(newPuzzleTuple)
            visitedPCMTuple.add(newPuzzleTuple)
    # Urutkan dulu isi dari tempListPuzzleTuple
    hasFound = anyHasReachTarget(tempListPCMTuple)
    for i in tempListPCMTuple:
        listPCMTuple.append(i)
    listPCMTuple = sortListPCMTuple(listPCMTuple)
    return hasFound, listPCMTuple, visitedPCMTuple

# TODO:
# def solvePuzzle(PuzzleTuple):
#     # Dipanggil dengan syarat puzzle bisa diselesaikan
#     currentMinimum = 99999 # Asumsi awal supaya bisa dioverride sama nilai goal value yang pertama
#     listPuzzleTuple = []
#     row, col = whereIsEmptyBlock(PuzzleTuple.myPuzzle())

