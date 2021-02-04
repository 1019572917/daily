class Solution:
    def allCellsDistOrder(self, R, C, r0, c0):
        rec = [(i,j) for i in range(R) for j in range(C)]
        rec.sort(key = lambda x: abs(x[0] - r0) + abs(x[1] - c0))
        return rec
