class Solution:
    def wordPattern(self, pattern, sr):
        s = sr.split()
        S,P= {},{}
        if len(pattern) != len(s):
            return False
        length = len(pattern)
        for i in range(length):
            if s[i] not in S:
                S[s[i]] = pattern[i]
            if pattern[i] not in P:
                P[pattern[i]] = s[i]
            if S.get(s[i]) != pattern[i] or P.get(pattern[i]) != s[i]:
                return False
        return True
