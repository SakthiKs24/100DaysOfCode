class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# Get input from user
nums_input = input("Enter numbers separated by commas: ")
target_input = int(input("Enter target number: "))

# Convert string input to list of integers
nums = list(map(int, nums_input.split(',')))
target = target_input

# Call the function
sol = Solution()
result = sol.twoSum(nums, target)
print("Output:", result)