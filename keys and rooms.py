class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited=[]
        
        #implement queue
        queue= [] 
        
        #store zero position in queue
        queue.append(0)
        
        #implement bfs
        while(queue):
            pos=queue.pop(0)
            
            #if the rooms is not visited yet then add it to queue else leave it 
            if(pos not in visited):
                visited.append(pos)
                
                #add add the room keys to queue 
                for i in rooms[pos]:
                    queue.append(i)
        
        #if all rooms are visted then the len of visited and len of rooms should be equal        
        return len(rooms)==len(visited)
        
        
