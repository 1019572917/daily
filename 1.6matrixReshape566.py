class Solution:
    def matrixReshape(self, nums, r, c):
        import numpy as np
        row,cloum = len(nums),len(nums[0])
        if r * c != row * cloum:
            return nums
        a = np.reshape(nums,(r,c))
        return a
