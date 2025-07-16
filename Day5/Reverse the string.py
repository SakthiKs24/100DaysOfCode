class Solution(object):
    def reverseWords(self, s):
        return " ".join(s.split()[::-1])

# Get user input
s = input("Enter a sentence: ")
# Create an object of the class
sol = Solution()
# Call the method and print the result
print("Reversed words:", sol.reverseWords(s))