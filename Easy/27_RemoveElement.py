class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        length = len(nums)
        i=0
        
        while i < length:
            
            if nums[i]==val:
                del nums[i]
                i-=1
                length-=1
        
            i+=1