
# CANT PUSH COULD NOT PROPERLY GOT THE OPTIMIZED SOLUTION


def isValidSudoku(board):
    
    # row checkup
    for i in range(len(board)):
        row_set = set()
        
        for j in range(len(board[i])):
            if board[i][j] in row_set:
                return False
            if board[i][j]!=".":
               row_set.add(board[i][j])
        
    # column checkup
    
    for i in range(len(board)):
        col_set = set()
        
        for j in range(len(board)):
            if board[j][i] in col_set:
                return False
            if board[j][i] !=".":
                col_set.add(board[j][i])
                
    # grid check
    # this works in a way like completes row and cols in 3 pairs at once
    for box_row in range(3):
        for box_col in range(3):
            
            box_set = set()
            
            for i in range(3):
                res = []
                for j in range(3):
                    val = board[box_row*3+i][box_col*3+j]
                    if val==".":
                        continue
                    if val in box_set:
                        return False
                    box_set.add(val)
                print(res)
    
    return True
    

board =[
    ["1","2",".",".","3",".",".",".","."],
    ["4",".",".","5",".",".",".",".","."],
    [".","9","8",".",".",".",".",".","3"],
    ["5",".",".",".","6",".",".",".","4"],
    [".",".",".","8",".","3",".",".","5"],
    ["7",".",".",".","2",".",".",".","6"],
    [".",".",".",".",".",".","2",".","."],
    [".",".",".","4","1","9",".",".","8"],
    [".",".",".",".","8",".",".","7","9"]
 ]

print(isValidSudoku(board))