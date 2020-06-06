class Solution {
    public int lengthOfLIS(int[] nums) {
        
        int[] piles = new  int[nums.length];
        int numpiles=0;
        
        for(int num: nums)
        {
            int destpile = Arrays.binarySearch(piles,0,numpiles,num);
            
            if (destpile < 0) {
                destpile = -(destpile + 1);
            }
            piles[destpile]=num;
            
            if (destpile == numpiles) {
                numpiles++;
            }
        }
        
        return numpiles;
        }
}
