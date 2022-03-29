import numpy as np

def random_matrix():
    # Buat untuk main.py pake fungsi random ukuran 1 sampai 16 (nanti pas print, 16 = _)
    # return matrix
    rng = np.random.default_rng()
    matrix = rng.choice(16, size=(4,4), replace=False)
    for i in range(4):
        for j in range(4):
            matrix[i][j] += 1
            print(matrix[i][j], end=" ")
        print()
    return matrix