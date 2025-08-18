class Solution:
    def sortColors(self, nums):
        low, mid, high = 0, 0, len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        return nums


if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers (0,1,2) separated by space: ").split()))
    sol = Solution()
    result = sol.sortColors(nums)
    print("Sorted colors:", result)
