from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)

        for word in strs:
            sorted_word = tuple(sorted(word))
            anagram_map[sorted_word].append(word)

        return list(anagram_map.values())

user_input = input("Enter words separated by space: ")
strs = user_input.strip().split()
sol = Solution()
result = sol.groupAnagrams(strs)
print("Grouped Anagrams:", result)
