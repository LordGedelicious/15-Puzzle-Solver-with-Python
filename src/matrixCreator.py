import numpy as np
import bNb
import os

def random_matrix():
    # Buat untuk main.py pake fungsi random ukuran 1 sampai 16
    # Pembuatan puzzle random menggunakan fungsi default_rng dari numpy.random
    # Penggunaan parameter replace = False agar tidak ada angka yang sama
    rng = np.random.default_rng()
    puzzle = rng.choice(16, size=(16), replace=False)
    for i in range(16):
        puzzle[i] += 1
    puzzle = np.array(puzzle)
    resultPTuple = bNb.PuzzleTuple(puzzle, 0, 0)
    return resultPTuple

def readFromFile():
    # Buat untuk main.py pake fungsi readFromFile
    # Pengambilan path directory menggunakan absolute path komputer pengguna
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