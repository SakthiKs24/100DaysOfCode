class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        next_greater = {}
        stack = []

        for number in reversed(nums2):
            while stack and stack[-1] <= number:
                stack.pop()

            if not stack:
                next_greater[number] = -1
            else:
                next_greater[number] = stack[-1]

            stack.append(number)

        result = []
        for number in nums1:
            result.append(next_greater[number])

        return result

if __name__ == "__main__":
    nums1 = list(map(int, input("Enter elements of nums1 separated by space: ").split()))
    nums2 = list(map(int, input("Enter elements of nums2 separated by space: ").split()))
        
    sol = Solution()
    result = sol.nextGreaterElement(nums1, nums2)

    print("Next greater elements are:", result)
