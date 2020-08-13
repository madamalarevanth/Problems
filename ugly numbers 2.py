class Solution:
    #dp
    def nthUglyNumber(self, n):
        #initialize an array and set arry [0]=1
        uglyNumbers =[1]
        
        #initialise three pointer variables p2,p3,p5 for 2,3,5
        p2,p3,p5 =0,0,0
        
        while len(uglyNumbers) < n:
            #If a value lesser than latest was already added, try finding next least value.
            if uglyNumbers[p2]*2 <= uglyNumbers[-1]:
                p2 += 1
                continue
            
            if uglyNumbers[p3]*3 <= uglyNumbers[-1]:
                p3 += 1
                continue
            
            if uglyNumbers[p5]*5 <= uglyNumbers[-1]:
                p5 += 1
                continue
            
            nextVal = min(uglyNumbers[p2]*2, uglyNumbers[p3]*3, uglyNumbers[p5]*5)
            uglyNumbers.append(nextVal)
        
        return uglyNumbers[-1]
