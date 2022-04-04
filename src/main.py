from asyncio.windows_events import NULL
from queue import PriorityQueue
import matrixCreator
import bNb
import time
import numpy as np
import os

def mainProgram():
    print("Selamat datang di program 15-Puzzle Solver")
    pathDirectory = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'output'))
    targetFile = input("Silahkan input nama file txt untuk menyimpan puzzle yang ingin dicari solusinya (tanpa extension .txt): ")
    targetFilePath = pathDirectory + "/" + targetFile + ".txt"
    targetFilePath = targetFilePath.replace("\\", "/")
    f = open(targetFilePath, "w")
    print("Silahkan pilih metode input matriks puzzle")
    print("1. Random")
    print("2. Read From File")
    choice = input("Silahkan masukkan metode pilihan anda: ")
    while not choice.isdigit() and choice != "1" and choice != "2":
        choice = input("Error. Please input a choice in range of 1 to 2: ")
    choice = int(choice)
    if choice == 1:
        print("Anda memakai random input", file=f)
        initPTuple = matrixCreator.random_matrix()
        initPTuple.printPuzzle(f)
        isSolvable = bNb.checkIsSolvable(initPTuple, f)
    elif choice == 2:
        initPTuple, fileNameWithExtension = matrixCreator.readFromFile()
        print("Anda memakai input dari file {}".format(fileNameWithExtension), file=f)
        initPTuple.printPuzzle(f)
        isSolvable = bNb.checkIsSolvable(initPTuple, f)
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
                timeTaken = time.time() - startTime
                printResult(initPTuple, currentMoveMade, timeTaken, nodeCreated, f)
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
                        prioQueue.put((newPuzzle.countCost() - currentNode[1], currentNode[1] - 1, [newPuzzle, currentMoveMade + [move]]))
    else:
        print("Puzzle is not solvable!", file=f)
    print("Hasil perhitungan dan kalkulasi sudah ditulis di file {}".format(targetFilePath))
    f.close()

def translateLangkah(langkah):
    if langkah == 'U':
        return "Atas"
    elif langkah == 'D':
        return "Bawah"
    elif langkah == 'L':
        return "Kiri"
    elif langkah == 'R':
        return "Kanan"

def printResult(initPTuple, currentMoveMade, timeTaken, nodeCreated, f):
    print("Waktu yang dibutuhkan: %.5f detik" %timeTaken, file=f)
    print("Jumlah node yang dibuat:", nodeCreated, file=f)
    print("Jumlah langkah yang dilakukan:", len(currentMoveMade), file=f)
    print("Semua langkah yang dilakukan:", currentMoveMade , file=f)
    stepCount = 1
    while len(currentMoveMade) != 0:
        langkah = currentMoveMade.pop(0)
        textLangkah = translateLangkah(langkah)
        print("Langkah ke-%d" %stepCount, ":", file=f)
        print("Move yang dilakukan:", textLangkah, file=f)
        initPTuple = bNb.moveTile(initPTuple, bNb.whereEmptyBlock(initPTuple), langkah)
        initPTuple.printPuzzle(f)
        stepCount += 1


mainProgram()

