class Solution:
  
  def check(self,row,col,grid):
    return 0<=row and row<=len(grid) and 0<=col and col<=len(grid[0]) and grid[row][col]== '1'
    
  def bfs(self,grid,row,col):
    queue=[]
    queue.append([row,col])
    
    while queue:
      popped = queue[0]
      row,col = popped[0],popped[1]
      
      //define direction in which we have to search the land 
      directions = [[row+1,col],[row-1,col],[row,col+1],[row,col-1]]
      
      for new_row, new_col in directions:
        if self.check(new_row,new_col,grid):
          grid[row][col]='0'
          queue.append([new_row,new_col])
      
      
  def def numIslands(self, grid: List[List[str]]) -> int:
    if not grid or not(grid[0]):
      return 0;
    
    h = len(grid)
    w= len(grid[0])
    answer=0
    
    for row in range(h):
      for col in range(w):
        if grid[row][col]=='1':
          answer+=1
          grid[row][col]='0'
          self.bfs(grid,row,col)
    return answer
