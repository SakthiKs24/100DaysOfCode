class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char_index_map = {}
        start = 0
        max_len = 0

        for end in range(len(s)):
            current_char = s[end]

            if current_char in char_index_map and char_index_map[current_char] >= start:
                start = char_index_map[current_char] + 1

            char_index_map[current_char] = end
            max_len = max(max_len, end - start + 1)

        return max_len

# 🔹 User Input
if __name__ == "__main__":
    s = input("Enter a string: ")
    sol = Solution()
    result = sol.lengthOfLongestSubstring(s)
    print("Length of the longest substring without repeating characters is:", result)
