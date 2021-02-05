class Solution:
    def nextGreaterElement(self, nums1, nums2):
        dic = {}
        stack = []
        for i in nums2:
            while stack and stack[-1] < i:
                dic[stack.pop()] = i
            stack.append(i)
        return [dic.get(i,-1) for i in nums1]
