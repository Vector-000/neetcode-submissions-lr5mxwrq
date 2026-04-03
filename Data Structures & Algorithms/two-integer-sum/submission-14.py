class Solution:
    def twoSum(self, nums, target):
        empty_dict = {}
        for i, num in enumerate(nums):
            ans = target-num
            if ans in empty_dict:
                return [empty_dict[ans], i]
            else:
                empty_dict[num] = i

