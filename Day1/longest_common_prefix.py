class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if prefix == "":
                    return ""
        return prefix

if __name__ == "__main__":
    user_input = input("Enter strings separated by commas: ")
    strs = [s.strip() for s in user_input.split(',')]  # convert input string to list
    solution = Solution()
    result = solution.longestCommonPrefix(strs)
    print("Longest common prefix:", result)