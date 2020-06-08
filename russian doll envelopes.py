class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        if n<=1:
            return n
        
        # sort the list in ascending order of their width and descending order of their height 
        envelopes.sort(key= lambda x: (x[0],-x[1]))
        
        #find the longest increasing subsequence
        size=0
        tail=[]
        
        #implementing patience sort
        for _,h in envelopes:
            l= bisect.bisect_left(tail,h)
            
            if l< len(tail):
                tail[l]=h
            else:
                tail.append(h)
                size = max(size,l+1)
        
        return size
                
