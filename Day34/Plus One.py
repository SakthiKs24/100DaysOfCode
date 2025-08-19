class Solution(object):
    def plusOne(self, digits):
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] = digits[i] + 1
                return digits
        return [1] + digits


if __name__ == "__main__":
    user_input = input("Enter a number: ")

    digits = [int(d) for d in user_input]

    sol = Solution()
    result = sol.plusOne(digits)

    print("Result as list:", result)
    print("Result as number:", "".join(map(str, result)))
