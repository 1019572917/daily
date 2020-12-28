class Solution:
    def threeSum(self, nums):
        length = len(nums)
        answer = []
        nums.sort()
        if length < 3:
            return []
        for i in range(length):
            if(i > 0 and nums[i] == nums[i-1]):
                continue
            l = i+1
            r = length - 1
            while l < r:
                if (nums[i] + nums[l] + nums[r] == 0):
                    answer.append([nums[i],nums[l],nums[r]])
                    while(l < r and nums[l] == nums[l+1]):
                        l += 1
                    while(l < r and nums[r] == nums[r-1]):
                        r -= 1
                    l += 1
                    r -= 1
                elif(nums[i] + nums[l] + nums[r] < 0):
                    l += 1
                elif(nums[i] + nums[l] + nums[r] > 0):
                    r -= 1
        return answer
