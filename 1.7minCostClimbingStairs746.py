class Solution:
    def minCostClimbingStairs(self, cost):
        length = len(cost)
        mincost0 = 0
        mincost1 = min(cost[0],cost[1])
        for i in range(2,length):
            mincost = min((mincost0 + cost[i - 1]),(mincost1 + cost[i]))
            mincost0,mincost1 = mincost1,mincost
        return mincost
