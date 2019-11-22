import pdb
def spiral_matrix(matrix)-> list:
    # pdb.set_trace()
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

data_array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
row = 5
d = [data_array[i:i + row] for i in range(0,len(data_array),row)]
# print([d[i][:] for i in range(0,len(d))])
res = spiral_matrix(d)
# print(res)

def spiral(n):
    dx,dy = 1,0            # Starting increments
    x,y = 0,0              # Starting location
    myarray = [[None]* n for j in range(n)]
    for i in range(n**2):
        myarray[x][y] = i
        nx,ny = x+dx, y+dy
        if 0<=nx<n and 0<=ny<n and myarray[nx][ny] == None:
            x,y = nx,ny
        else:
            dx,dy = -dy,dx
            x,y = x+dx, y+dy
    return myarray
def printspiral(myarray):
    n = range(len(myarray))
    for y in n:
        for x in n:
            print (myarray[x][y])
        print('')
# print(printspiral(spiral(5)))
spi = spiral(5)
spi_2 = zip(*spi)
for i in  spi_2:
    print(i)