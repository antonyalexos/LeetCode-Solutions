class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        def accumu(lis):
            total = 0
            for x in lis:
                total += x
                yield total
            return total
        return max(list(accumu(gain))) if max(list(accumu(gain)))>0 else 0