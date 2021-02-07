class Solution:
    def backspaceCompare(self, S, T):
        lists,listt = [],[]
        for i in S:
            if i == "#" and lists == []:
                lists = []
            elif i == "#" and lists != []:
                lists.pop()
            else:
                lists.append(i)
        for i in T:
            if i == "#" and listt == []:
                listt = []
            elif i == "#" and listt != []:
                listt.pop()
            else:
                listt.append(i)
        return lists == listt
