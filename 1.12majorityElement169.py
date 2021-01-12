class Solution:
    def majorityElement(self, nums):
        count = 0
        major = 0
        for num in nums:
            if count == 0:
                major = num
            if num == major:
                count += 1
            else:
                count -= 1
        return major
