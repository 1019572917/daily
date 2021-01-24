class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        length = len(nums)
        if length == 1:
            return nums[0]
        mincost0 = nums[0]
        mincost1 = max(nums[0],nums[1])
        for i in range(2,length):
            mincost = max((mincost0 + nums[i]),mincost1)
            mincost0,mincost1 = mincost1,mincost
        return mincost1
