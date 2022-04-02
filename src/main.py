# Buatlah program dalam Java/Python untuk menyelesaikan persoalan 15-Puzzle dengan
# menggunakan Algoritma Branch and Bound seperti pada materi kuliah. Nilai bound tiap
# simpul adalah penjumlahan cost yang diperlukan untuk sampai suatu simpul x dari akar,
# dengan taksiran cost simpul x untuk sampai ke goal. Taksiran cost yang digunakan adalah
# jumlah ubin tidak kosong yang tidak berada pada tempat sesuai susunan akhir (goal state). 

import matrix
import branchNbound
import time

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
            t0= time.time()
            isChoiceCorrect = True
            newPuzzle = matrix.random_matrix()
            newPuzzleTuple = branchNbound.PCMTuple(newPuzzle, 0, 0, 0)
            boolSolvable = branchNbound.isSolvable(newPuzzleTuple)
            branchNbound.printMatrix(newPuzzleTuple)
            if boolSolvable:
                print("Solvable!")
                listPuzzleTuple = branchNbound.moveTiles(newPuzzleTuple, [])
                branchNbound.printListPuzzleTuple(listPuzzleTuple)
                hasFoundTarget = branchNbound.anyHasReachTarget(listPuzzleTuple)
                while not(hasFoundTarget):
                    listPuzzleTuple = branchNbound.moveTiles(newPuzzleTuple, listPuzzleTuple)
                    hasFoundTarget = branchNbound.anyHasReachTarget(listPuzzleTuple)
                t1 = time.time() - t0
                print("Time elapsed: ", t1) # CPU seconds elapsed (floating point)
                print("OKE DAH KELAR")
                exit()
            else:
                print("Puzzle is unsolvable!")
                exit()
            # Buat dari matrix.py pake fungsi random
        elif choice == 2:
            t0= time.time()
            isChoiceCorrect = True
            newPuzzleTuple = branchNbound.PCMTuple(matrix.readFromFile(), 0, 0, 0)
            boolSolvable = branchNbound.isSolvable(newPuzzleTuple)
            branchNbound.printMatrix(newPuzzleTuple)
            visitedPCMTuple = set()
            if boolSolvable:
                print("Solvable!")
                hasFoundTarget, listPuzzleTuple, visitedPCMTuple = branchNbound.moveTiles(newPuzzleTuple, [], visitedPCMTuple)
                while not(hasFoundTarget):
                    hasFoundTarget, listPuzzleTuple, visitedPCMTuple = branchNbound.moveTiles(newPuzzleTuple, listPuzzleTuple, visitedPCMTuple)
                t1 = time.time() - t0
                print("Time elapsed: ", t1) # CPU seconds elapsed (floating point)
                print("OKE DAH KELAR")
                exit()
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