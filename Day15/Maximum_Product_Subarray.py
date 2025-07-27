class Solution(object):
    def maxProduct(self, nums):
        max_ending_here = nums[0]
        min_ending_here = nums[0]
        max_so_far = nums[0]

        for n in nums[1:]:
            if n < 0:
                max_ending_here, min_ending_here = min_ending_here, max_ending_here

            max_ending_here = max(n, max_ending_here * n)
            min_ending_here = min(n, min_ending_here * n)

            max_so_far = max(max_so_far, max_ending_here)

        return max_so_far


nums = list(map(int, input("Enter numbers separated by space: ").split()))

solution = Solution()
print("Maximum Product Subarray:", solution.maxProduct(nums))
