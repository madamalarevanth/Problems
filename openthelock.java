class Solution {
    public int openLock(String[] deadends, String target) {
        
        //store all the deadends in hashset for constant lookups
        HashSet<String> dead_ends = new HashSet(Arrays.asList(deadends));
        
        //store the visited
        HashSet<String> visited = new HashSet();
        visited.add("0000");
        
        //queue for bfs
        Queue<String> q = new LinkedList();
        q.offer("0000");
        
        //to store the level of tree we are at a given instance
        int level =0;
        
        //implementing bfs
        while(!q.isEmpty())
        {
            //notes the no of nodes in queue in current level
            int size = q.size();
            
            //take out each node from queue and bfs its children
            while(size>0)
            {
                String lock_position = q.poll();
                
                //if deadlock leave that combination
                if(dead_ends.contains(lock_position))
                {
                    size--;
                    continue;
                }
                
                //target found return the level number which is number of moves we made
                if(lock_position.equals(target))
                    return level;
                
                //if not form all the possible combinations i.e by increasing oro decreasing the number by 1 at each of the face values
                StringBuilder sb = new StringBuilder(lock_position);
                for(int i=0;i<4;i++)
                {
                    char curr = sb.charAt(i);
                    String s1 = sb.substring(0,i)+ (curr=='9'? 0: curr-'0'+1)+sb.substring(i+1);
                    String s2 = sb.substring(0,i)+ (curr=='0'? 9: curr-'0'-1)+sb.substring(i+1);
                   
                   // if the new string is not visited yet and not a deadend add it to visited and push it into queue
                    if(!visited.contains(s1) && !dead_ends.contains(s1))
                    {
                        q.offer(s1);
                        visited.add(s1);
                    }
                    
                     if(!visited.contains(s2) && !dead_ends.contains(s2))
                    {
                        q.offer(s2);
                        visited.add(s2);
                    }
                }
                //decrease the size of queue after traversing the elements of it 
                size--;
            }
            //increase the level number as we move on 
            level++;
        }
        return -1;
    }
}
