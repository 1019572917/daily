class Solution:
    def threeSumClosest(self, nums, target):
        length = len(nums)
        nums.sort()
        a = nums[0] + nums[1] + nums[2]
        if length < 3:
            return []
        for i in range(length):
            if(i > 0 and nums[i] == nums[i-1]):
                continue
            l = i+1
            r = length - 1
            while l < r:
                if(nums[i] + nums[l] + nums[r] == target):
                    return target
                elif(nums[i] + nums[l] + nums[r] < target):
                    if (abs(target - a) > abs(target - nums[i] - nums[l] - nums[r])):
                        a = nums[i] + nums[l] + nums[r]
                    while(l < r and nums[l] == nums[l+1]):
                        l += 1
                    l += 1
                else:
                    if (abs(target - a) > abs(target - nums[i] - nums[l] - nums[r])):
                        a = nums[i] + nums[l] + nums[r]
                    while(l < r and nums[r] == nums[r-1]):
                        r -= 1
                    r -= 1
        return a
