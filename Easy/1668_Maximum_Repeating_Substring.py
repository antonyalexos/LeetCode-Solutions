class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        if len(word) > len(sequence): return 0
        cnt=1
        while word*cnt in sequence:
            cnt+=1
        return cnt-1