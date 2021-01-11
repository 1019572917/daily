class Solution:
    def singleNumber(self, nums):
        nums.sort()
        length = len(nums)
        if length == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[length - 1] != nums[length - 2]:
            return nums[length - 1]
        for i in range(length - 1):
            if nums[i] != nums[i + 1] and nums[i] != nums[i - 1]:
                return nums[i]
