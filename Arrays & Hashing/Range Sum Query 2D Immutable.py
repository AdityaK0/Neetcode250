
from sys import prefix
from typing import List


class NumMatrix:
    
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        rows = len(matrix)
        cols = len(matrix[0])
        self.prefixMat = [[ 0 for c in range(cols+1) ] for r in range(rows+1)]
        
        
        for r in range(rows):
            for c in range(cols):
                self.prefixMat[r+1][c+1] = self.prefixMat[r+1][c]+self.prefixMat[r][c+1]+self.matrix[r][c] - self.prefixMat[r][c]
                
        
        
        
        # upper row calculation
        # self.prefixMat[0][0] =  self.matrix[0][0]
        # for c in range(1,cols):
        #     self.prefixMat[0][c] = self.prefixMat[0][c-1]+self.matrix[0][c]
        
        # # # left column calculation
        
        # for r in range(1,rows):
        #     self.prefixMat[r][0] = self.prefixMat[r-1][0]+self.matrix[r][0]
        
        # # # fill matrixes 
        
        # for r in range(1,rows):
        #     for c in range(1,cols):
        #         above = self.prefixMat[r-1][c]
        #         left = self.prefixMat[r][c-1]
        #         topleft  = self.prefixMat[r-1][c-1]
        #         self.prefixMat[r][c] = self.matrix[r][c]+above+left - topleft
                
        # current rowise current_col-left 
        # upper_part = current_row-1 went to upper part 
        # that row[current_place_where need ] to store the value 
        
        

    def sumRegion(self, row1, col1, row2, col2):
        for mats in self.prefixMat:
            print(mats,"\n")
        
        row1+=1
        row2+=1
        col1+=1
        col2+=1
        breakpoint()
        return (self.prefixMat[row2][col2] - self.prefixMat[row2][col1-1] - self.prefixMat[row1-1][col2] + self.prefixMat[row1-1][col1-1])
            
        # full_area = self.prefixMat[row2][col2]
        
        # if row1>0:
        #    top_part = self.prefixMat[row1-1][col2]
        #    full_area-=top_part
        # if col1>0:
        #    left_part = self.prefixMat[row2][col1-1]
        #    full_area-=left_part
        
        # if row1>0 and col1>0:
        #    topLeft = self.prefixMat[row1-1][col1-1] # as we removed this twice so need add back once
        #    full_area+=topLeft
           
        
        # return full_area
        
        
        
        # grid_sum = 0 # normal flow to calculate the rectangle
        # for r in range(row1,row2+1):
        #     for c in range(col1,col2+1):
        #         grid_sum+=self.matrix[r][c]

        # return grid_sum  
        
        
        
        # grid_sum = 0
        
        
        
        # if row1 == row2:
        #     for i in range(col1,col2+1):
        #         grid_sum+=self.matrix[row1][i]
        #     return grid_sum    
       
        # for k in range(col1,col2+1,1):
        #     grid_sum+=self.matrix[row1][k]
                
        # # step 2 : create lower part
        
        # for j in range(col2,col1-1,-1):
        #     grid_sum+=self.matrix[row2][j]
        
 

        # # step 3 : middle part remaining rows row1+1(as we have already covered row1 ) to row2
        # for r in range(row1+1,row2,1):
        #     for c in range(col1,col2+1):
        #         grid_sum+=self.matrix[r][c]

        # return grid_sum             

numMatrix = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])

print(numMatrix.sumRegion(2, 1, 4, 3))
print(numMatrix.sumRegion(1, 1, 2, 2))
print(numMatrix.sumRegion(1, 2, 2, 4))


numMatrix = NumMatrix([[0,1,2],[3,4,5],[6,7,8]])

print(numMatrix.sumRegion(0,0,2,2))
print(numMatrix.sumRegion(1,1,1,2))
print(numMatrix.sumRegion(0,1,1,2))



# if row1 == row2 

# why this condition is needed because its saves us to not count the same number in same row

# example 

# [ 1  2  3  4 ]
# [ 5  6  7  8 ]
# [ 9 10 11 12 ]

# row1 = 1 , col1 = 1 , row2 = 1 , col2= 3

# now if u see wee need to add the all element of the rectangle every thing came 
# (0,1) or whatever at once but if the both rows are same then its just a slice 
# of an array when there are highly chances of counting the same number again 
# then will endup having same number calculated again when will calculate the bottom part 

# Step 1 (top row) from col1 -> col2+1
# 6 + 7 + 8 = 21
# Step 2 (bottom row — same row again!)
# 8 + 7 + 6 = 21  from col2 -> col1-1 

# in the above example we got ended up as the same count again so when this scenario comes
# just count only once and return the answer 