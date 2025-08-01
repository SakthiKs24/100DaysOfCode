class Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return 1
        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

# Get user input
n = int(input("Enter number of steps: "))
solution = Solution()
print("Number of distinct ways to climb:", solution.climbStairs(n))