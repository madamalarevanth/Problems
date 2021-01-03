
class Solution:
    def knapSack(self, N, W, val, wt):
        dp = [0 for i in range(W+1)]
        
        for i in range(W+1):
            for j in range(N):
                if(wt[j]<=i):
                    dp[i] = max(dp[i],dp[i-wt[j]]+val[j])
        return dp[W]
