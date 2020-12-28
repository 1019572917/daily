class Solution:
    def removeDuplicates(self, nums):
        nums.sort()
        length = len(nums)
        i = 0
        j = 1
        if length == 1:
            return len(nums)
        while j <= length - 1:
            if nums[i] == nums[j]:
                j += 1
                continue
            if nums[i] != nums[j]:
                i +=1 
                nums[i] = nums[j]
        return len(nums[:i+1])
