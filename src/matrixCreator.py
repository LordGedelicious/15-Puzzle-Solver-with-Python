import numpy as np
import bNb
import os

def random_matrix():
    # Buat untuk main.py pake fungsi random ukuran 1 sampai 16 (nanti pas print, 16 = _)
    # return puzzle
    rng = np.random.default_rng()
    puzzle = rng.choice(16, size=(16), replace=False)
    for i in range(16):
        puzzle[i] += 1
    puzzle = np.array(puzzle)
    resultPTuple = bNb.PuzzleTuple(puzzle, 0, 0)
    return resultPTuple

def readFromFile():
    pathDirectory = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'input'))
    filename = input("Masukkan nama file (tanpa extension .txt): ")
    filePath = pathDirectory + "/" + filename + ".txt"
    filePath = filePath.replace("\\", "/")
    f = open(filePath, "r")
    puzzle = [int(i) for i in f.read().split()]
    puzzle = np.array(puzzle)
    resultPTuple = bNb.PuzzleTuple(puzzle, 0, 0)
    filenameExtension = filename + ".txt"
    return resultPTuple, filenameExtension

def readConsole():
    # Implementasi belakangan aja setelah main.py
    puzzle = []
    for i in range(0, 16):
        elmnt = int(input())
        puzzle.append(elmnt) # adding the element
    puzzle = np.array(puzzle)
    resultPTuple = bNb.PuzzleTuple(puzzle, 0, 0)
    return resultPTuple