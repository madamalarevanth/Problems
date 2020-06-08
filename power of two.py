class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        if n==1:
            return True
        
        s= format(n,'b')
        count=0
        
        for i in s:
            if i=='1':
                count+=1;
            if count>1:
                return False
        return True
