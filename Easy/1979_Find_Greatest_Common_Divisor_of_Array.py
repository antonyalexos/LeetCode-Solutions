class Solution:
    def findGCD(self, nums: List[int]) -> int:
        minimum = min(nums)
        maximum = max(nums)
        div = 1
        for i in range(1,min(nums)+1):
            if minimum%i == maximum%i == 0:
                div = i
        return div