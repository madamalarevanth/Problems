class Solution {
    
    //keeps track of number of solutions
    int count=0;
    
    public int findTargetSumWays(int[] nums, int S) {
        
        calculate(nums,0,0,S);
        
        return count;
        
    }
    
    public void calculate(int[] nums,int i, int sum,int S)
    {
        if(i==nums.length)
        {
            if(S==sum)
                count++;
            else
                return ;
        }
        else
        {
            calculate(nums,i+1,sum+nums[i],S);
            calculate(nums,i+1,sum-nums[i],S);
        }
    }
    
}
