from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        #Count how many times each number appears
        count = Counter(nums)  

        #Create empty buckets - one list for each possible frequency
        freq = [[] for _ in range(len(nums) + 1)]  

        #Place numbers into buckets based on their frequency
        for num, c in count.items():
            freq[c].append(num)

        #Go through buckets from highest frequency to lowest
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:  # If we already have k numbers, stop
                    return res


nums = list(map(int, input("Enter numbers separated by space: ").split()))
k = int(input("Enter k (top frequent count): "))

solution = Solution()
result = solution.topKFrequent(nums, k)
print("Top", k, "frequent elements are:", result)
