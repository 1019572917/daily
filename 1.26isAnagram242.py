class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        length = len(s)
        dicts,dictt = {},{}
        for i in range(length):
            if s[i] not in dicts:
                dicts[s[i]] = 0
            if t[i] not in dictt:
                dictt[t[i]] = 0
            dicts[s[i]] += 1
            dictt[t[i]] += 1

        return dicts == dictt
