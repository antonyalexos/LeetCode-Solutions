class Solution:
    def minOperations(self, logs: List[str]) -> int:
        cnt = 0
        for x in logs:
            if x == "../":
                if cnt>0:
                    cnt -= 1
            elif x != "./":
                cnt += 1
        return max(0,cnt)