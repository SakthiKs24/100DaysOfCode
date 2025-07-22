class Solution(object):
    def strStr(self, haystack, needle):
        return haystack.find(needle)

haystack = input("Enter the haystack string: ")
needle = input("Enter the needle string: ")

sol = Solution()
result = sol.strStr(haystack, needle)

print("Result:", result)
