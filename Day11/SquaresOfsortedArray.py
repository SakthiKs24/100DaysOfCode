class Solution(object):
    def sortedSquares(self, nums):
        n = len(nums)
        res = [0] * n
        left, right = 0, n - 1
        i = n - 1

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                res[i] = nums[left] ** 2
                left += 1
            else:
                res[i] = nums[right] ** 2
                right -= 1
            i -= 1

        return res

input_str = input("Enter a sorted array (comma-separated): ")
nums = list(map(int, input_str.strip().split(',')))

sol = Solution()
result = sol.sortedSquares(nums)

print("Sorted squares:", result)
