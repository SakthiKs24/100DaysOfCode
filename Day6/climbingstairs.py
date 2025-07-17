class Solution(object):
    def climbStairs(self, n):
        def climb(n):
            if n == 1:
                return 1
            if n == 2:
                return 2
            return climb(n - 1) + climb(n - 2)
        return climb(n)

# Get user input
n = int(input("Enter number of steps: "))
solution = Solution()
print("Number of distinct ways to climb:", solution.climbStairs(n))
