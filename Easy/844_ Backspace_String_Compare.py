class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        tmp_s = ''
        tmp_t = ''
        i = len(s)-1
        j = len(t)-1
        for i in range(len(s)):
            if s[i] == '#':
                tmp_s = tmp_s[:-1]
            else: 
                tmp_s += s[i]
        for i in range(len(t)):
            if t[i] == '#':
                tmp_t = tmp_t[:-1]
            else: 
                tmp_t += t[i]
        return tmp_s==tmp_t