def empty_location(grid,l):
    for row in range(9):
        for col in range(9):
            if(grid[row][col]== 0):
                l[0]= row
                l[1]= col
                return True
    return False
    
#chk if num is used in that row
def used_in_row(grid,r,num):
    for i in range(9):
        if(grid[r][i] == num):
            return True
    return False

#chk if num is used in that column
def used_in_column(grid,c,num):
    for i in range(9):
        if(grid[i][c] == num):
            return True
    return False

#chk if num is used in that box
def used_in_box(grid,r,c,num):
    for i in range(3):
        for j in range(3):
            if(grid[r+i][c+j] == num):
                return True
    return False

#chk if condition is not violated   
def safe(grid,r,c,i):
    #it is safe only if that number is not already used in that column, row and box
    return not used_in_row(grid,r,i) and not used_in_column(grid,c,i) and not used_in_box(grid,r-r%3,c-c%3,i)
    
def solve_sudoku(grid):
    
    ##l stores the empty location that needs to be filled by the number
    l=[0,0] #row,col
    
    if( not empty_location(grid,l)):
        return True
        
    #assign the row and col for entering number
    row,col = l[0],l[1]
    
    #for all digits 1- 9
    for i in range(1,10):
        if (safe(grid,row,col,i)):
            grid[row][col]= i
            
            #recursion
            if(solve_sudoku(grid)):
                return True
            
            #incase it backtracked
            grid[row][col]= 0
    
    return False

def print_grid(arr):

    for i in range(9):
        for j in range(9):
            print(arr[i][j],end=" ")
    print()
