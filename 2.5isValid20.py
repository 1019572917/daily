class Solution:
    def isValid(self, s):
        dic = {"(" : ")","[" : "]","{" : "}",1:1}
        stack = [1]
        for i in s:
            if i in dic:
                stack.append(i)
            else:
                if dic[stack.pop()] != i:
                    return False
        return stack == [1]
