class Solution:
    
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        
        #get the set of valid directions or neighbors
        def valid_neighbors(i,j,d):
            for x,y in [[1,0],[-1,0],[0,1],[0,-1]]:
                ni,nj,nd = i+x,j+y,d+1
                
                #checking validity of the neighbors
                if 0<=ni<len(matrix) and 0<= nj<len(matrix[0]):
                    yield ni,nj,nd
        
        #perform bfs search for the nearest 0 value 
        def bfs(i,j):
            
            q=collections.deque([(i,j,0)])#last value denotes the distance
            
            while(q):
                i,j,d = q.popleft()
                
                for ni,nj,nd in valid_neighbors(i,j,d):
                    if matrix[ni][nj]==0:
                        return nd
                    q.append((ni,nj,nd))
            return
            
            
        R= len(matrix)
        C= len(matrix[0])
        
        for i  in range(R):
            for j in range(C):
                
                if(matrix[i][j] !=0):
                    matrix[i][j]= bfs(i,j)
        return matrix    
