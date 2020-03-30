class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        if not s:
            return 0
        
        try:
            last_word = s.split()[-1]
        except IndexError:
            return 0
        return len(last_word)