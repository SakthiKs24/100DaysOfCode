class Solution(object):
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"

        # Initialize result array with 0s
        res = [0] * (len(num1) + len(num2))

        # Reverse both strings
        num1 = num1[::-1]
        num2 = num2[::-1]

        # Multiply digit by digit
        for i in range(len(num1)):
            for j in range(len(num2)):
                digit1 = ord(num1[i]) - ord('0')
                digit2 = ord(num2[j]) - ord('0')
                res[i + j] += digit1 * digit2
                res[i + j + 1] += res[i + j] // 10
                res[i + j] %= 10

        # Remove leading zeros
        while len(res) > 1 and res[-1] == 0:
            res.pop()

        # Convert result array to string
        return ''.join(str(d) for d in res[::-1])


if __name__ == "__main__":
    num1 = input("Enter first number: ").strip()
    num2 = input("Enter second number: ").strip()

    solution = Solution()
    result = solution.multiply(num1, num2)
    print("Product:", result)
