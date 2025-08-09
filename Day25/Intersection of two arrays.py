class Solution(object):
    def intersection(self, nums1, nums2):
        seen = set(nums1)   # Store unique elements from nums1
        result = set()      # Store intersection elements

        for num in nums2:
            if num in seen:
                result.add(num)  # Ensures uniqueness

        return list(result)

nums1 = list(map(int, input("Enter nums1 (space-separated): ").split()))
nums2 = list(map(int, input("Enter nums2 (space-separated): ").split()))

sol = Solution()
print("Intersection:", sol.intersection(nums1, nums2))
