class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1

nums = list(map(int, input("Enter sorted numbers separated by space: ").split()))
target = int(input("Enter the target number: "))

sol = Solution()
result = sol.search(nums, target)

if result != -1:
    print(f"Target found at index {result}")
else:
    print("Target not found in the list")
