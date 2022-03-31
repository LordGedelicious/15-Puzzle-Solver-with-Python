import numpy as np
import os

def random_matrix():
    # Buat untuk main.py pake fungsi random ukuran 1 sampai 16 (nanti pas print, 16 = _)
    # return puzzle
    rng = np.random.default_rng()
    puzzle = rng.choice(16, size=(4,4), replace=False)
    for i in range(4):
        for j in range(4):
            puzzle[i][j] += 1
    return puzzle

def readFromFile():
    pathDirectory = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'input'))
    filename = input("Masukkan nama file (tanpa extension .txt): ")
    filePath = pathDirectory + "/" + filename + ".txt"
    filePath = filePath.replace("\\", "/")
    puzzle = []
    f = open(filePath, "r")
    for row in f:
        puzzle.append([int(x) for x in row.split()])
    return puzzle

# def readConsole():
# Implementasi belakangan aja setelah main.py