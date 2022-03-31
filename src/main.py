# Buatlah program dalam Java/Python untuk menyelesaikan persoalan 15-Puzzle dengan
# menggunakan Algoritma Branch and Bound seperti pada materi kuliah. Nilai bound tiap
# simpul adalah penjumlahan cost yang diperlukan untuk sampai suatu simpul x dari akar,
# dengan taksiran cost simpul x untuk sampai ke goal. Taksiran cost yang digunakan adalah
# jumlah ubin tidak kosong yang tidak berada pada tempat sesuai susunan akhir (goal state). 

import matrix
import branchNbound

import numpy as np

def main():
    print("Selamat datang di 15-Puzzle Solver!")
    print("Silahkan pilih opsi untuk inisiasi matriks puzzle:")
    print("1. Random")
    print("2. Manual (from txt file)")
    print("3. Manual (from console)")
    isChoiceCorrect = False
    while not(isChoiceCorrect):
        choice = int(input("Pilihan anda: "))
        if choice == 1:
            isChoiceCorrect = True
            newPuzzle = matrix.random_matrix()
            newPuzzleTuple = branchNbound.PCMTuple(newPuzzle, 0, 0)
            boolSolvable = branchNbound.isSolvable(newPuzzleTuple)
            branchNbound.printMatrix(newPuzzleTuple)
            if boolSolvable:
                print("Solvable!")
                emptyRow, emptyCol = branchNbound.whereIsEmptyBlock(newPuzzleTuple)
                listPuzzleTuple = branchNbound.moveTiles(newPuzzleTuple, [], emptyRow, emptyCol)
                branchNbound.printListPuzzleTuple(listPuzzleTuple)
            else:
                print("Puzzle is unsolvable!")
                exit()
            # Buat dari matrix.py pake fungsi random
        elif choice == 2:
            isChoiceCorrect = True
            newPuzzleTuple = branchNbound.PCMTuple(matrix.readFromFile(), 0, 0)
            boolSolvable = branchNbound.isSolvable(newPuzzleTuple)
            branchNbound.printMatrix(newPuzzleTuple)
            if boolSolvable:
                print("Solvable!")
                emptyRow, emptyCol = branchNbound.whereIsEmptyBlock(newPuzzleTuple)
                listPuzzleTuple = branchNbound.moveTiles(newPuzzleTuple, [], emptyRow, emptyCol)
                branchNbound.printListPuzzleTuple(listPuzzleTuple)
            else:
                print("Puzzle is unsolvable!")
                exit()
            # Buat dari matrix.py pake fungsi readTxtFile
        elif choice == 3:
            isChoiceCorrect = True
            # Buat dari matrix.py pake fungsi readConsole
        else:
            print("Pilihan tidak tersedia! Silahkan coba lagi.")

main()