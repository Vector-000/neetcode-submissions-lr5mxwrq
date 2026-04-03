class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            ans = seen.get(target - num)
            if (target - num) in seen:
                return [ans, i]
            else:
                seen[num] = i

