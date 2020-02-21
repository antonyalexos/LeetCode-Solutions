class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        j=0
        for i in nums[:]:
            del nums[0]
            j=j+1
            if((target-i) in nums):
                return j-1, nums.index(target-i)+j