class Solution:
    def largestPerimeter(self, A):
        A.sort()
        A = A[::-1]
        for i in range(len(A) - 2):
            if A[i + 1] + A[i + 2] > A[i] and A[i] - A[i + 2] < A[i + 1]:
                return A[i] + A[i + 1] + A[i + 2]
        return 0
