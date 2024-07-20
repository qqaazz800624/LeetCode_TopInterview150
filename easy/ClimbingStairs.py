#%%

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        
        dp = [i for i in range(n+1)]
        dp[1] = 1
        dp[2] = 2
        
        for k in range(3, n+1):
            dp[k] = dp[k-2] + dp[k-1]
        
        return dp[n]


#%%

Solution().climbStairs(3)



#%%





#%%






#%%