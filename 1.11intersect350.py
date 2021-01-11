class Solution:
    def intersect(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        length1 = len(nums1)
        length2 = len(nums2)
        l1 = 0
        l2 = 0
        answer = []
        while l1 < length1 and l2 < length2:
            if nums1[l1] == nums2[l2]:
                answer.append(nums1[l1])
                l1 += 1
                l2 += 1
            elif nums1[l1] < nums2[l2]:
                l1 += 1
            else:
                l2 += 1
        return answer
