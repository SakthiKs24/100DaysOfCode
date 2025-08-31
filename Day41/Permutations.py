class Solution(object):
    def permute(self, nums):
        result = []

        def backtrack(path, remaining):
            if not remaining:  
                result.append(path)
                return
            for i in range(len(remaining)):
                backtrack(path + [remaining[i]], remaining[:i] + remaining[i+1:])

        backtrack([], nums)
        return result


if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers separated by space: ").split()))
    sol = Solution()
    print("All permutations:")
    print(sol.permute(nums))
