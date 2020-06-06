class Solution {
    private int[] cumilative_weights;
    private int sum;

    public Solution(int[] w) {
        sum=0;
        cumilative_weights = new int[w.length];
        
        for(int i=0;i<w.length;i++)
        {
            sum+=w[i];
            cumilative_weights[i]=sum;
        }
        
    }
    
    public int pickIndex() {
        int idx= (int)(Math.random()*sum);
        int index = Arrays.binarySearch(cumilative_weights,idx+1);
        if(index<0)
            return -index-1;
        return index;
    }
    
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(w);
 * int param_1 = obj.pickIndex();
 */
