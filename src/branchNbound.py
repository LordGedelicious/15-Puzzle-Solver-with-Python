import numpy as np

def isSolvable(puzzle):
    count = 0
    index = 1
    while (index <= 16):
        tempCount = 0
        col = index - 1
        row = index // 4
        if (index > 4):
            col = (index % 4) - 1
        if (index in [4,8,12,16]):
            row -= 1
        if (puzzle[row][col] == 16):
            if ((row + col) % 2 != 0):
                count += 1
            index += 1
            tempCount = 1
        else:
            currentValue = puzzle[row][col]
            # Menggunakan urutan 1 sampai 16
            for i in range(0, 4):
                for j in range(0, 4):
                    indexProcessed = i * 4 + (j + 1)
                    if (indexProcessed > index and puzzle[i][j] < currentValue):
                        count += 1
                        tempCount += 1
            index += 1
        print("Now processing row {} and col {}, value is {}, add {} to count".format(row, col, puzzle[row][col], tempCount))
    if (count % 2 == 0):
        print("Solvable")
    else:
        print("Not solvable")
    return count