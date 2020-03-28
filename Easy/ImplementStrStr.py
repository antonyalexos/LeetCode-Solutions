class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if not needle:
            return 0
        
        try:
            return haystack.index(needle)
        except ValueError:
            return -1