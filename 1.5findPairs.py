class Solution:
    def findPairs(self, nums, k):
        answer = 0
        length = len(nums)
        nums.sort()
        j = 0
        for i in range(length):
            if i >= 1 and nums[i] == nums[i - 1]:
                continue
            for j in range(i+1,length):
                if abs(nums[j] - nums[i]) == k:
                    answer += 1
                    break
        return answer
