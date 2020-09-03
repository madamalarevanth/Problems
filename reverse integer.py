class Solution:
    def reverse(self, x: int) -> int:
        sign = lambda x: (1, -1)[x < 0] 
        val = int(str(abs(x))[::-1])
        rev = sign(x)*val
        
        return rev if rev.bit_length()<32 else 0
