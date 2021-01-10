class Solution:
    def intersection(self, nums1, nums2):
        length1 = len(nums1)
        length2 = len(nums2)
        nums1.sort()
        nums2.sort()
        p1 = 0
        p2 = 0
        answer = set()
        while p1 < length1 and p2 < length2:
            if nums1[p1] == nums2[p2]:
                answer.add(nums1[p1])
                p1 += 1
                p2 += 1
            elif nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                p2 += 1
        return list(answer)
