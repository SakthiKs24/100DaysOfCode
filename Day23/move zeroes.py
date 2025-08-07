class Solution(object):
    def moveZeroes(self, nums):
        j = 0  # Position to place the next non-zero

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

# Get user input as comma-separated integers
input_str = input("Enter numbers separated by commas (e.g., 0,1,0,3,12): ")
nums = list(map(int, input_str.split(',')))

# Create Solution instance and call the method
sol = Solution()
sol.moveZeroes(nums)

# Print the modified list
print("After moving zeroes:", nums)
