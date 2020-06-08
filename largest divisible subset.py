class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums)==0:
            return []
        
        final_list=[]
        #sort the array to get all the divisors of an number before that number 
        nums.sort(reverse=False)
        
        #create a variable list to store the size of divisible subset till that point 
        divcount= [1 for i in range(len(nums))]
        
        #create var to store previous divisor index for a given subset
        prev = [-1 for i in range(len(nums)) ]
        
        #store the index of largest element in the longest subset
        max_ind=0
        
        #initiate the algorithm
        # for each i we find the longest divisible subset formed till the ith index
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] % nums[j]==0:
                    if divcount[i]<divcount[j]+1:
                        divcount[i]= divcount[j]+1
                        prev[i]=j
                        
            #update max_ind
            if divcount[max_ind] < divcount[i]: 
                max_ind = i 
        
        #dummy variable to traverse nums list to get the longest divisible subset
        k= max_ind
        
        while(k>=0):
            final_list.append(nums[k])
            k=prev[k]
        
        return final_list
                        
