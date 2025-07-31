class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def binarySearch(leftBias):
            left, right = 0, len(nums) - 1
            index = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    index = mid
                    if leftBias:
                        right = mid - 1  
                    else:
                        left = mid + 1 
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return index

        return [binarySearch(True), binarySearch(False)]


if __name__ == "__main__":
    nums = list(map(int, input("Enter sorted list of numbers (space-separated): ").split()))
    target = int(input("Enter the target value: "))
    
    solution = Solution()
    result = solution.searchRange(nums, target)
    
    print("First and Last Position of Target:", result)
