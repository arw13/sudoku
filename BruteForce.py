# Brute force solving of sudoku#

import numpy as np
import pdb
import time

# Start Timer
startTime = time.time()
# Sample sudoku

# CountSudoku = np.array([[0, 0, 6, 0, 0, 8, 5, 0, 0],
#                         [0, 0, 0, 0, 7, 0, 6, 1, 3],
#                         [0, 0, 0, 0, 0, 0, 0, 0, 9],
#                         [0, 0, 0, 0, 9, 0, 0, 0, 1],
#                         [0, 0, 1, 0, 0, 0, 8, 0, 0],
#                         [4, 0, 0, 5, 3, 0, 0, 0, 0],
#                         [1, 0, 7, 0, 5, 3, 0, 0, 0],
#                         [0, 5, 0, 0, 6, 4, 0, 0, 0],
#                         [3, 0, 0, 1, 0, 0, 0, 6, 0]])

# Impossible Puzzleeeee
impossible = np.array([[0, 0, 0, 0, 0, 5, 0, 8, 0],
                       [0, 0, 0, 6, 0, 1, 0, 4, 3],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 1, 0, 5, 0, 0, 0, 0, 0],
                       [0, 0, 0, 1, 0, 6, 0, 0, 0],
                       [3, 0, 0, 0, 0, 0, 0, 0, 5],
                       [5, 3, 0, 0, 0, 0, 0, 6, 1],
                       [0, 0, 0, 0, 0, 0, 0, 0, 4],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0]])

# Brute force solver

def CheckForDubs(sudoku):
    for nums in range(1,10):
        #check columns for doubles
        for cols in range(0,9):
            dubcheck = np.extract(sudoku[:,cols] == nums, sudoku)
            if len(dubcheck.tolist()) > 1:
                return 1 #dubcheck

        # check rows for doubles
        for rows in range(0,9):
            dubcheck = np.extract(sudoku[rows, :] == nums, sudoku)
            if len(dubcheck.tolist()) > 1:
                return 2 #dubcheck

        # check boxes for doubles
        for i in range(0,7,3):
            for j in range(0,7,3):
                dubcheck = np.extract(sudoku[i:i+3, j:j+3] == nums, sudoku)
                if len(dubcheck.tolist()) > 1:
                    return 3 # dubcheck
    else:
        return 0

#collect immutable numbers
def Sudone(mat_in):
    sudoku = np.copy(mat_in)
    done = 0
    col = 0
    row = 0
<<<<<<< HEAD
<<<<<<< HEAD

=======
    m = 1 # momentum
>>>>>>> momentum
=======
    m = 1 # momentum

>>>>>>> aefd14038cba0c5cef896380fd5b4f1d02340391
    while done is 0:
        while (CheckForDubs(sudoku) !=0 or m != 0) and sudoku[row, col]<9 :
            if mat_in[row,col]==0:
                sudoku[row, col] +=1 # add one to cell number
                m = 0
            else:
                break

        if CheckForDubs(sudoku) !=0 or m == -1:
            if mat_in[row,col]==0:
                sudoku[row, col] = 0 # clear cell
            col -= 1 # move back one cell
            m = -1

        if m >= 0:
            col +=1 # move forward one cell
            m = 1


        if col == -1:
            col = 8  # move backwards up a row
            row -=1  # move to next row
        elif col == 9:
            col = 0    # new row
            row += 1   # move down one cell



        print(sudoku, end="\r", flush=True)
        # time.sleep(.1)

        # done = True*((col == 9 and row == 9) or (col == 0 and row < 0))
        done = True*(row > 8 or row < 0)

    return sudoku

# pdb.set_trace()
X = Sudone(impossible)
print(X)
print('CheckForDubs(solution) =', CheckForDubs(X))
print("--- %s seconds ---" % (time.time() - startTime))
