class Solution:
    def findDuplicate(self, nums):
        length = len(nums)
        nums.sort()
        for i in range(length - 1):
            if nums[i] == nums[i + 1]:
                return nums[i]
