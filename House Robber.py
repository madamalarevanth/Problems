#Recursion
#according to the logic we cant rob adjacent houses, so at a given instant or index (i) we can only rob house[i] or house[i-1]. so to decide which gives the max 
#consider total sum that ie if we rob house[i] we can also rob house[i-2] or we can only rob house[i-1]. so lets take the max of these max(house[i]+house[i-2],house[i].
#lets implement it in recursion

def rob(self, nums: List[int]) -> int:
        #recursion
        def stealFromHouse(index):
            #base case 
            if index >= len(nums):
                return 0
            #recursion
            return max( nums[index]+stealFromHouse(index+2),stealFromHouse(index+1))
        
        return stealFromHouse(0)
      
#for Dp solution
#maintain an maxGold[dp array] which stores the max gold possible while robbing house i 
#follow the same formula we can either loot curr house + max looted till curr-2 house or loot prev house. choose the max between these two and keep updating

 if len(nums)==1:
            return nums[0]
        if len(nums)==0:
            return 0
        
        maxGold=[nums[0],max(nums[0],nums[1])]
        
        for i in range(2,len(nums)):
            curr= nums[i]
            prevmax = maxGold[i-1]
            prev_of_prevmax = maxGold[i-2]
            maxGold.append(max(prev_of_prevmax+curr,prevmax))
        
        return maxGold[len(nums)-1]
 
#dp optimised for constant space 
#instead of maintain an array of maxGOld for ith house maintain two dummy varible of curr, current max and previous max
#curr is ith gold , current max is max gold possible if choosen previous house and previous max is max gold possible if choosen i-2 th house 
#implement same logic on it as previous
def rob(self, nums: List[int]) -> int:
        currMax=0
        prevMax=0
        
        for i in range(len(nums)):
            curr= nums[i]
            newMax = max(curr+prevMax,currMax)
            prevMax = currMax
            currMax = newMax
        
        return currMax

      
