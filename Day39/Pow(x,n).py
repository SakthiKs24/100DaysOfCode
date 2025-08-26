class Solution(object):
    def myPow(self, x, n):
        if n == 0: return 1.0
        if n < 0:
            x, n = 1 / x, -n
        
        result = 1.0
        while n > 0:
            if n % 2 == 1:
                result *= x
            x *= x
            n //= 2
        return result

if __name__ == "__main__":
    x = float(input("Enter the value of x: "))
    n = int(input("Enter the value of n: "))

    s = Solution()
    ans = s.myPow(x, n)
    print(f"{x}^{n} = {ans}")
