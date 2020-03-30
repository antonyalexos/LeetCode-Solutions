class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max1 = nums[0]
        max2 = max1
        
        length = len(nums)
        
        for i in range(1,length):
            max1 = max(nums[i], max1 + nums[i])
            max2 = max(max1,max2)
            
        return max2