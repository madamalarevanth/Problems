class Solution:
    def numSquares(self, n: int) -> int:
        
        if n<4:
            return n
        
        #collect all the possible square till n 
        lst=[]
        i=1
        while i*i <=n:
            lst.append(i*i)
            i+=1
            
        to_check = {n}
        
        #store the depth we have traversed the tree
        cnt=0;
        
        #bfs search 
        while to_check:
            cnt+=1
            
            #temp set to store the possible childrens of given root   
            temp= set()
            
            #checking if x==y if not subtract y from x and store it to check in next level
            for x in to_check:
                for y in lst:
                    if x<y:
                        break
                    if x==y:
                        return cnt
                    temp.add(x-y)
            
            #change the check list with new updated list 
            to_check= temp
        return cnt
    
    
        
