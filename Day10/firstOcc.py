class Solution(object):
    def strStr(self, haystack, needle):
        n, m = len(haystack), len(needle)

        if m == 0:
            return 0  

        for i in range(n - m + 1):
            if haystack[i:i + m] == needle:
                return i
        return -1

haystack = input("Enter the haystack string: ")
needle = input("Enter the needle string: ")

sol = Solution()
result = sol.strStr(haystack, needle)

print("Result: ", result)
