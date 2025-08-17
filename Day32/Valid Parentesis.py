class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping:
                if not stack or mapping[char] != stack.pop():
                    return False
        return not stack


if __name__ == "__main__":
    s = input("Enter the string containing brackets: ")
    sol = Solution()
    result = sol.isValid(s)
    print("Valid" if result else "Invalid")
