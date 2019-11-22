# import numpy as np
import pdb
""" Methodology: 
1. Print the first row.
for the rest of the rows:
    2. ptint the last column,
    3. print the last row in reverse
    4. print the first column """

def spiral_matrix(matrix:list)-> list:
    result = []
    #Handling edge cases:
    if len(matrix) == 0:
        return []
    if len(matrix) == 1:
        return matrix[0]

    row = len(matrix)
    col = len(matrix[0])
    # print(row,col)
    r = c = 0
    iter = 0
    max_iter = min(row,col)
    # print("row = {},col = {}".format(row,col))
    result = []
    while iter < max_iter:
        # print(result)
        if iter % 2 == 0:
            for j in range(c, col):
                result.append(matrix[r][j])

            for i in range(r+1,row):
                result.append(matrix[i][col-1])
                # print(i)
            r = r + 1
            col = col -1

        else:
            for i in reversed(range(c,col)):
                result.append(matrix[row-1][i])
            for j in reversed(range(r,row-1)):
                result.append(matrix[j][c])
            c = c+1
            row = row - 1
        iter +=1
    return result


input = [[1,2,3,4,5,6],
    [7,8,9,10,11,12],
    [13,14,15,16,17,18],
    [19,20,21,22,23,24],
    [25,26,27,28,29,30],
    # [31,32,33,34,35,36]
    ]
res = spiral_matrix(input)

spiral_array = [res[i:i+6] for i in range(0,len(res),6)]
# print(spiral_array)