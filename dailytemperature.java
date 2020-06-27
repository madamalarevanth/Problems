class Solution {
    public int[] dailyTemperatures(int[] T) {
        int[] ans = new int[T.length];
        Stack<Integer> stack = new Stack();
        
        for(int i=T.length-1;i>=0;i--)
        {
            //if the current temperature is greater than the temp of 
            //index of stack we can remove the tempin stack and store the new value 
            //cuz it will be the nearer and larger temp   
            while(!stack.isEmpty() && T[i]>=T[stack.peek()])
                stack.pop();
            
            //if stack is empty its either last element or there exist no higher temperature
            ans[i]=stack.isEmpty()? 0: stack.peek()-i;
            
            //push the current temperature index into stack 
            stack.push(i);
        }
        
        return ans;
    }
}
