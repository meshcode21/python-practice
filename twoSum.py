class Solution:
    def twoSum(self, a, t):
        for i in range(len(a)):
            for j in range(i + 1, len(a)):
                if a[i] + a[j] == t:
                    return [i, j]
        return []

arr = [2,7,11,15]
target = 9

result = Solution().twoSum(arr, target)

print(result)
