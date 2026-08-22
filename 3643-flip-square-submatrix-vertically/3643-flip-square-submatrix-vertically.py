import math
class Solution(object):
    def reverseSubmatrix(self, grid, x, y, k):
        if k/2<=1:
            for i in range(y,y+k):
                grid[x][i],grid[x+k-1][i]=grid[x+k-1][i],grid[x][i]
        else:
            for j in range (0,int(math.ceil(k/2))):
                for i in range(y,y+k):
                    grid[x+j][i],grid[x+k-1-j][i]=grid[x+k-1-j][i],grid[x+j][i]
        return grid