from asyncio.windows_events import NULL
import numpy as np
import copy

class PCMTuple: # PCMTuple = Puzzle Cost Move Tuple
    def __init__(self, puzzle, cost, moveMade):
        # Puzzle adalah matrix numpy 4x4
        # Cost adalah cost dari puzzle tersebut (bukan nilai RETURN(i))
        # Awalnya nilai cost adalah 0
        self.puzzle = puzzle
        self.cost = cost
        self.moveMade = moveMade
    
    def containedPuzzle(self):
        return self.puzzle
    
    def containedCost(self):
        return self.cost
    
    def containedMoveMade(self):
        return self.moveMade
    
    def copy(self, PuzzleTuple):
        return PCMTuple(PuzzleTuple.containedPuzzle(), PuzzleTuple.containedCost(), PuzzleTuple.containedMoveMade())

def printMatrix(PCMTuple):
    matrix = PCMTuple.containedPuzzle()
    for i in range(4):
        for j in range(4):
            print(matrix[i][j], end=" ")
        print()

def printPuzzle(puzzle):
    for i in range(4):
        for j in range(4):
            print(puzzle[i][j], end=" ")
        print()

def measureInitScore(PCMTuple):
    puzzle = PCMTuple.containedPuzzle()
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
    matrix = PCMTuple.containedPuzzle()
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
        return ['RIGHT', 'UP', 'LEFT']
    elif (col == 0 and row != 0 and row != 3):
        return ['RIGHT', 'DOWN', 'UP']
    elif (col == 3 and row != 0 and row != 3):
        return ['LEFT', 'DOWN', 'UP']
    else:
        return ['RIGHT', 'DOWN', 'UP', 'LEFT']
        
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
            if (listPCMTuple[j].containedCost() < listPCMTuple[minimum].containedCost()):
                minimum = j
        temp = listPCMTuple[i]
        listPCMTuple[i] = listPCMTuple[minimum]
        listPCMTuple[minimum] = temp
    return listPCMTuple

def anyHasReachTarget(listPCMTuple):
    for i in range(len(listPCMTuple)):
        countCorrect = 0
        nowTestingPuzzle = listPCMTuple[i].containedPuzzle()
        print()
        printPuzzle(nowTestingPuzzle)
        for j in range(0, 4):
            for k in range(0, 4):
                if (nowTestingPuzzle[j][k] == (j*4 + k + 1)):
                    countCorrect += 1
        print("Skor : ", countCorrect)
        if (countCorrect == 16):
            return True
    return False

def moveTiles(firstPCMTuple, listPCMTuple, row, col):
    # Dibagi jadi dua kondisi
    # Pertama, kalau untuk inisiasi pertama kali, dia diurutkan berdasarkan cost
    # Kedua, kalau udah move >= 1, simpul dengan cost terendah selanjutnya bakal dimajuin ke depan queue, sisanya ke belakang
    tempListPCMTuple = []
    if (len(listPCMTuple) == 0):
        baselinePuzzle = firstPCMTuple.containedPuzzle()
        countMoveMade = 0
    else:
        baselinePCMTuple = listPCMTuple.pop(0)
        baselinePuzzle = baselinePCMTuple.containedPuzzle()
        countMoveMade = baselinePCMTuple.containedMoveMade()
    # Buat dulu semua kemungkinan puzzle yang bisa dibuat
    possibleMoves = whereCanTileMove(row, col)
    for move in possibleMoves:
        indexPuzzle = copy.deepcopy(baselinePuzzle)
        if (move == 'RIGHT'):
            newPuzzle = switchTwoValuesInMatrix(indexPuzzle, row, col, row, col + 1)
        elif (move == 'LEFT'):
            newPuzzle = switchTwoValuesInMatrix(indexPuzzle, row, col, row, col - 1)
        elif (move == 'UP'):
            newPuzzle = switchTwoValuesInMatrix(indexPuzzle, row, col, row - 1, col)
        elif (move == 'DOWN'):
            newPuzzle = switchTwoValuesInMatrix(indexPuzzle, row, col, row + 1, col)
        newPuzzleCost = costAliveNodes(newPuzzle, countMoveMade + 1)
        tempListPCMTuple.append(PCMTuple(newPuzzle, newPuzzleCost, countMoveMade + 1))
    # Urutkan dulu isi dari tempListPuzzleTuple
    tempListPCMTuple = sortListPCMTuple(tempListPCMTuple)
    # Masukkan ke listPuzzleTuple
    listPCMTuple = tempListPCMTuple
    hasFoundTarget = anyHasReachTarget(listPCMTuple)
    while not(hasFoundTarget):
        print("BELUM KETEMU ITERASI KE " + str(countMoveMade))
        row, col = whereIsEmptyBlock(listPCMTuple[0])
        listPCMTuple = moveTiles(firstPCMTuple, listPCMTuple, row, col)
        hasFoundTarget = anyHasReachTarget(listPCMTuple)
        if (hasFoundTarget):
            print("YEY KETEMU ITERASI KE " + str(countMoveMade))
            printListPuzzleTuple(listPCMTuple)
            return listPCMTuple
    return listPCMTuple

def printListPuzzleTuple(listPuzzleTuple):
    for i in range(len(listPuzzleTuple)):
        printMatrix(listPuzzleTuple[i])
        print(listPuzzleTuple[i].containedCost())
        print(listPuzzleTuple[i].containedMoveMade())

# TODO:
# def solvePuzzle(PuzzleTuple):
#     # Dipanggil dengan syarat puzzle bisa diselesaikan
#     currentMinimum = 99999 # Asumsi awal supaya bisa dioverride sama nilai goal value yang pertama
#     listPuzzleTuple = []
#     row, col = whereIsEmptyBlock(PuzzleTuple.containedPuzzle())

