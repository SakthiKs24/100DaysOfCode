class Solution(object):
    def removeElement(self, nums, val):
        k = 0 
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  
                k += 1
        return k

if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers (space-separated): ").split()))
    val = int(input("Enter the value to remove: "))

    sol = Solution()
    k = sol.removeElement(nums, val)

    print("k =", k)
    print("Modified array =", nums[:k])  
