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
        # Inisiasi jumlah simpul awal, waktu awal, dan dictionary untuk menyimpan puzzle yang pernah ditemukan
        nodeCreated = 0
        startTime = time.time()
        visitedStates = dict()
        # Isi dari priorityQueue : (cost, kedalaman (negatif), [puzzle, dictionary])
        # Empat blok dibawah ini adalah inisiasi awal dari informasi simpul root
        prioQueue = PriorityQueue()
        currentMoveMade = []
        prioQueue.put((0, -1, [initPTuple, currentMoveMade]))
        visitedStates[initPTuple.returnPuzzleBytes()] = True
        # Fungsi loop yang akan break/keluar ketika menemukan solusi
        hasFound = False
        while not hasFound:
            # Akan mengambil elemen pertama dari priority queue dan mengecek apakah puzzle yang ditampung merupakan solusi atau bukan
            currentNode = prioQueue.get()
            currentTuple = currentNode[2][0]
            currentMoveMade = currentNode[2][1]
            if currentTuple.isGoal():
                hasFound = True
                timeTaken = time.time() - startTime
                printResult(initPTuple, currentMoveMade, timeTaken, nodeCreated, f)
            else:
                # Bila bukan solusi, maka akan dilakukan perulangan berdasarkan semua langkah yang mungkin dilakukan dari posisi petak kosong pada puzzle simpul tersebut
                currentEmptyBlockIdx = bNb.whereEmptyBlock(currentTuple)
                currentMoveList = bNb.whereToMove(currentEmptyBlockIdx)
                for move in currentMoveList:
                    newPuzzle = bNb.moveTile(currentTuple.copy(), currentEmptyBlockIdx, move)
                    newPuzzle.setCost = newPuzzle.countCost()
                    newPuzzle.setMoveMade(len(currentMoveMade) + 1)
                    # Simpul baru hanya ditambahkan jika belum pernah ditemukan sebelumnya state puzzlenya
                    if newPuzzle.returnPuzzleBytes() not in visitedStates.keys():
                        nodeCreated += 1
                        visitedStates[newPuzzle.returnPuzzleBytes()] = True
                        # Kedalaman suatu simpul disimpan dalam bentuk currentNode[1]
                        # Semakin negatif nilai currentNode[1], maka posisi simpul semakin dalam
                        # Untuk dua simpul dengan cost yang sama, maka prioritas akan jatuh kepada simpul yang lebih dalam
                        prioQueue.put((newPuzzle.countCost() - currentNode[1], currentNode[1] - 1, [newPuzzle, currentMoveMade + [move]]))
    else:
        print("Puzzle is not solvable!", file=f)
    print("Hasil perhitungan dan kalkulasi sudah ditulis di file {}".format(targetFilePath))
    f.close()

def translateLangkah(langkah):
    # Langkah disimpul dalam bentuk char untuk membantu mempermudah penulisan dan debugging
    # Char akan ditranslasi menjadi string untuk memudahkan pengguna mengerti output file
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
    # Output puzzle dan langkah yang dilakukan dari awal hingga solusi
    while len(currentMoveMade) != 0:
        langkah = currentMoveMade.pop(0)
        textLangkah = translateLangkah(langkah)
        print("Langkah ke-%d" %stepCount, ":", file=f)
        print("Move yang dilakukan:", textLangkah, file=f)
        initPTuple = bNb.moveTile(initPTuple, bNb.whereEmptyBlock(initPTuple), langkah)
        initPTuple.printPuzzle(f)
        stepCount += 1


mainProgram()

