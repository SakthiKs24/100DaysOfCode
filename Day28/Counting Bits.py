class Solution(object):
    def countBits(self, n):
        ans = []
        for i in range(n + 1):
            binary_representation = bin(i)      
            count_ones = binary_representation.count('1')  
            ans.append(count_ones)             
        return ans

sol = Solution()

n = int(input("Enter a number n: "))

result = sol.countBits(n)

print("Count of 1's in binary from 0 to", n, "is:")
print(result)
