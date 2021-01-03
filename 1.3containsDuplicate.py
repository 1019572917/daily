class Solution:
    def containsDuplicate(self, nums):
        length = len(nums)
        if length == 1:
            return False
        nums.sort()
        for i in range(length - 1):
            if nums[i] == nums[i+1]:
                return True
        return False
