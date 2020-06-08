/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        
    int low=1 ,high = n;
    int least=n; 
        
        while(low<=high)
        {
            int mid = low+ (high-low)/2;
            boolean val =isBadVersion(mid);
            if (val== true )
            {
                    high = mid-1;
                    if(least>mid)
                        least = mid;
            }
            else
                low = mid+1;        
                
        }
        return least;
    }
}
