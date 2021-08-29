class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        cnt = 0
        for i in range(len(s)):
            if s[i] in vowels and i<len(s)/2:
                cnt += 1
            elif s[i] in vowels and i+1>len(s)/2:
                cnt -= 1
        return cnt==0