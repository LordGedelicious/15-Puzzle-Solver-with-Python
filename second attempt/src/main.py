from secrets import choice
import matrixCreator
import bNb

def main():
    print("Selamat datang di program 15-Puzzle Solver")
    print("Silahkan pilih metode input matriks puzzle")
    print("1. Random")
    print("2. Read From File")
    print("3. Read From Command Line Interface")
    choice = input("Please input an integer: ")
    while not choice.isdigit():
        choice = input("Error. Please input an INTEGER: ")
    choice = int(choice)
    if choice == 1:
        print("Kamu pakai random input")
        initPTuple = matrixCreator.random_matrix()
        initPTuple.printPuzzle()
    elif choice == 2:
        print("Kamu pakai input dari file")
        initPTuple = matrixCreator.readFromFile()
        initPTuple.printPuzzle()
    elif choice == 3:
        print("Kamu pakai input dari command line interface")

main()

