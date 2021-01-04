class Solution:
    def moveZeroes(self, nums):
        length = len(nums)
        j = 0
        if length == 0:
            return
        for i in range(length):
            if nums[i]:
                nums[j],nums[i] = nums[i],nums[j]
                j += 1
