class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        
        return i + 1


input_str = input("Enter sorted numbers separated by space: ")
nums = list(map(int, input_str.strip().split()))

sol = Solution()
k = sol.removeDuplicates(nums)

print(f"\nNumber of unique elements: {k}")
