from queue import PriorityQueue
import matrixCreator
import bNb
import time
import numpy as np

def main():
    print("Selamat datang di program 15-Puzzle Solver")
    print("Silahkan pilih metode input matriks puzzle")
    print("1. Random")
    print("2. Read From File")
    print("3. Read From Command Line Interface")
    choice = input("Please input an integer: ")
    while not choice.isdigit() and choice != "1" and choice != "2" and choice != "3":
        choice = input("Error. Please input an integer in range of 1 to 3: ")
    choice = int(choice)
    if choice == 1:
        print("Kamu pakai random input")
        initPTuple = matrixCreator.random_matrix()
        initPTuple.printPuzzle()
        isSolvable = bNb.checkIsSolvable(initPTuple)
        bNb.solve(initPTuple)
    elif choice == 2:
        print("Kamu pakai input dari file")
        initPTuple = matrixCreator.readFromFile()
        isSolvable = bNb.checkIsSolvable(initPTuple)
        if (isSolvable):
            nodeCreated = 0
            startTime = time.time()
            visitedStates = dict()
            # Isi dari priorityQueue : (cost, kedalaman (negatif), [puzzle, dictionary])
            prioQueue = PriorityQueue()
            currentMoveMade = []
            prioQueue.put((0, -1, [initPTuple, currentMoveMade]))
            visitedStates[initPTuple.returnPuzzleBytes()] = True
            hasFound = False
            while not hasFound:
                currentNode = prioQueue.get()
                currentTuple = currentNode[2][0]
                currentMoveMade = currentNode[2][1]
                if currentTuple.isGoal():
                    hasFound = True
                    print("OKE KETEMU")
                    print("Waktu yang dibutuhkan adalah {} detik".format(time.time() - startTime))
                    print("Jumlah node yang dibuat adalah {}".format(nodeCreated))
                    print("Jumlah langkah yang dibutuhkan adalah {}".format(len(currentMoveMade)))
                else:
                    currentEmptyBlockIdx = bNb.whereEmptyBlock(currentTuple)
                    currentMoveList = bNb.whereToMove(currentEmptyBlockIdx)
                    for move in currentMoveList:
                        newPuzzle = bNb.moveTile(currentTuple.copy(), currentEmptyBlockIdx, move)
                        newPuzzle.setCost = newPuzzle.countCost()
                        newPuzzle.setMoveMade(len(currentMoveMade) + 1)
                        if newPuzzle.returnPuzzleBytes() not in visitedStates.keys():
                            nodeCreated += 1
                            visitedStates[newPuzzle.returnPuzzleBytes()] = True
                            prioQueue.put((newPuzzle.countCost(), currentNode[1] - 1, [newPuzzle, currentMoveMade + [move]]))
    elif choice == 3:
        print("Kamu pakai input dari command line interface")
        initPTuple = matrixCreator.readConsole()
        initPTuple.printPuzzle()

main()

