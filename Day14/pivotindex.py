class Solution(object):
    def pivotIndex(self, nums):
        total_sum = sum(nums)
        left_sum = 0

        for i, num in enumerate(nums):
            if left_sum == total_sum - left_sum - num:
                return i
            left_sum += num
        return -1

nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
sol = Solution()
print("Pivot Index:", sol.pivotIndex(nums))
