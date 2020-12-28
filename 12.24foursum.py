class Solution:
    def fourSum(self, nums, target):
        length = len(nums)
        nums.sort()
        answer = []
        if length < 4:
            return[]
        for i in range(length - 2):
            for j in range(length-1,2,-1):
                l = i + 1
                r = j - 1
                while l < r:
                    if (nums[i] + nums[l] + nums[r] + nums[j] == target and [nums[i],nums[l],nums[r],nums[j]] not in answer):
                        answer.append([nums[i],nums[l],nums[r],nums[j]])
                        while(l < r and nums[l] == nums[l + 1]):
                            l += 1
                        while(l < r and nums[r] == nums[r - 1]):
                            r -=1
                        l += 1
                        r -= 1
                    elif nums[i] + nums[l] + nums[r] + nums[j] < target:
                        l += 1
                    else:
                        r -= 1
        return answer
