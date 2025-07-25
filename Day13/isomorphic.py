class Solution(object):
    def isIsomorphic(self, s, t):
        pattern_s = []
        pattern_t = []
        for i in s:
            pattern_s.append(s.index(i))
        for i in t:
            pattern_t.append(t.index(i))
        return pattern_s == pattern_t

s = input("Enter first string: ")
t = input("Enter second string: ")

sol = Solution()
result = sol.isIsomorphic(s, t)


if result:
    print("True")
else:
    print("False")
