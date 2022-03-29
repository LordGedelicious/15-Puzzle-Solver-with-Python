import numpy as np

def measureCost(puzzle):
    count = 0
    index = 1
    while (index <= 16):
        col = index - 1
        row = index // 4
        if (index > 4):
            col = (index % 4) - 1
        if (index in [4,8,12,16]):
            row -= 1
        if (puzzle[row][col] == 16) and ((row + col) % 2 != 0):
            count += 1
        currentValue = puzzle[row][col]
        # Menggunakan urutan 1 sampai 16
        for i in range(0, 4):
            for j in range(0, 4):
                indexProcessed = i * 4 + (j + 1)
                if (indexProcessed > index and puzzle[i][j] < currentValue):
                    count += 1
        index += 1
    return count

def isSolvable(puzzle):
    initial_score = measureCost(puzzle)
    if (initial_score % 2 == 0):
        print("Solvable with a score of " + str(initial_score))
    else:
        print("Not solvable with a score of " + str(initial_score))