class Solution(object):
    def searchInsert(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left


nums = list(map(int, input("Enter sorted array elements (space separated): ").split()))
target = int(input("Enter target value: "))

solution = Solution()
result = solution.searchInsert(nums, target)
print("Output index:", result)
