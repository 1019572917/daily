class Solution:
    def sortArrayByParityII(self, A):
        o,j,answer = [],[],[]
        for i in A:
            if(i % 2 == 0):
                o.append(i)
            else:
                j.append(i)
        for i in range(len(o)):
            answer.append(o[i])
            answer.append(j[i])
        return answer
