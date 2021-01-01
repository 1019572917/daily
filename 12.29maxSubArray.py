class Solution:
    def maxSubArray(self, nums):
        length = len(nums)
        for i in range(1,length):
            if nums[i - 1] > 0:
                nums[i] += nums[i-1]
        return max(nums)
