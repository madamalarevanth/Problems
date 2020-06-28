class Solution {
    public int evalRPN(String[] tokens) {
        String operator="+-*/";
        
        Stack<String> stack = new Stack();
        
        for(String t: tokens)
        {
            if(!operator.contains(t))
                stack.push(t);
            else
            {
                int a = Integer.valueOf(stack.pop());
                int b = Integer.valueOf(stack.pop());
                
                int index= operator.indexOf(t);
                
                switch(index)
                {
                    case 0:
                        stack.push(String.valueOf(a+b));
                        break;
                    case 1:
                        stack.push(String.valueOf(b-a));
                        break;
                    case 2:
                        stack.push(String.valueOf(a*b));
                        break;
                    case 3:
                        stack.push(String.valueOf(b/a));
                        break;
                }
                
            }
                    
        }
        return Integer.valueOf(stack.pop());
    }
}
