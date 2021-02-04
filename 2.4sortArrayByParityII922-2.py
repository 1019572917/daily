class Solution:
    def sortArrayByParityII(self, A):
        o = 0
        j = 1
        answer = [0] * len(A)
        for i in A:
            if i % 2 == 0:
                answer[o] = i
                o += 2
            else:
                answer[j] = i
                j += 2
        return answer
