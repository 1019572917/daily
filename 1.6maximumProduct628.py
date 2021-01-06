class Solution:
    def maximumProduct(self, nums):
        length = len(nums)
        nums.sort()
        return max((nums[length - 1] * nums[length - 2] * nums[length - 3]),(nums[0] * nums[1] * nums[length - 1]))
