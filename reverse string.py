class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def helper(s,i,j):
            if i>j:
                return 
            s[i],s[j] = s[j],s[i]
            
            helper(s,i+1,j-1)
        
        helper(s,0,len(s)-1)
