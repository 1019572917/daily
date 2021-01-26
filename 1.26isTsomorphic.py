class Solution:
    def isIsomorphic(self, s, t):
        length = len(s)
        dicts,dictt = {},{}
        for i in range(length):
            if dicts.get(s[i]) != dictt.get(t[i]):
                return False
            else:
                dicts[s[i]] = dictt[t[i]] = i
        return True
