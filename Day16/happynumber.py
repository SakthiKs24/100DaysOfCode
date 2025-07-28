class Solution(object):
    def isHappy(self, n):
        def get_next(num):
            total = 0
            while num > 0:
                digit = num % 10
                total += digit * digit
                num //= 10
            return total

        slow = n
        fast = get_next(n)

        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))

        return fast == 1


if __name__ == "__main__":
    n = int(input("Enter a number: "))
    result = Solution().isHappy(n)
    print(f"{n} is a Happy Number? {result}")
