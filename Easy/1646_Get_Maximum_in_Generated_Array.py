class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums = [0]*(n+1)
        if n == 0: return 0
        elif n==1: return 1
        else:
            nums[1] = 1
            for i in range(2,n+1):
                if i%2==0:
                    nums[i] = nums[i//2]
                else:
                    nums[i] = nums[(i)//2] + nums[(i)//2+1]
            return max(nums)