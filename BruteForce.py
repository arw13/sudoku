# Brute force solving of sudoku#

import numpy as np
import pdb

# Sample sudoku

CountSudoku = np.array([[5, 0, 0, 0, 8, 0, 0, 4, 9],
                      [0, 0, 0, 5, 0, 0, 0, 3, 0],
                      [0, 6, 7, 3, 0, 0, 0, 0, 1],
                      [1, 5, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 2, 0, 8, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 1, 8],
                      [7, 0, 0, 0, 0, 4, 1, 5, 0],
                      [0, 3, 0, 0, 0, 2, 0, 0, 0],
                      [4, 9, 0, 0, 5, 0, 0, 0, 3]])

hasDubs = np.array([[5, 1, 0, 0, 8, 0, 0, 4, 9],
                      [0, 0, 1, 5, 0, 0, 0, 3, 0],
                      [0, 6, 7, 3, 0, 0, 0, 0, 1],
                      [1, 5, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 2, 0, 8, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 1, 8],
                      [7, 0, 0, 0, 0, 4, 1, 5, 0],
                      [0, 3, 0, 0, 0, 2, 0, 0, 0],
                      [4, 9, 0, 0, 5, 0, 0, 0, 3]])


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

# CheckforDubs test
# a = CheckForDubs(hasDubs)
# print(a)

#collect immutable numbers
def Sudone(mat_in):
    sudoku = np.copy(mat_in)
    done = 0
    col = 0
    row = 0
    
    while done is 0:
        while (CheckForDubs(sudoku) !=0 or sudoku[row, col] == 0) and sudoku[row, col]<10 :
            if mat_in[row,col]==0:
                sudoku[row, col] +=1
            else:
                col -= 1
        if CheckForDubs(sudoku) == 0 and sudoku[row, col]<10 :
            col +=1
            if col == 9:
               col = 0
               row += 1
        if CheckForDubs(sudoku) !=0 or sudoku[row, col]>9:
            if mat_in[row,col]==0:
                sudoku[row, col] = 0
            col -= 1
            if col == 0:
                col = 8
                row -=1


        print(sudoku, end='\r')
        done = True*((col == 9 and row == 9) or (col <= 0 and row <= 0))
    return sudoku

pdb.set_trace()
X = Sudone(CountSudoku)
print(X)
