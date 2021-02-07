class Solution:
    def calPoints(self, ops: List):
        answer = []
        for i in ops:
            if i == "C":
                answer.pop()
            elif i == "D":
                answer.append(answer[-1] * 2)
            elif i == "+":
                answer.append(answer[-1] + answer[-2])
            else:
                answer.append(int(i))
        return sum(answer)
