class Solution:
    def sortedSquares(self, nums):
        length = len(nums)
        for i in range(length):
            nums[i] = nums[i] ** 2
        nums.sort()
        return nums
