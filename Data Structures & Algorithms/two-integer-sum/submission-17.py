class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            ans = seen.get(target - num)
            if ans is not None:
                return [ans, i]
            seen[num] = i

