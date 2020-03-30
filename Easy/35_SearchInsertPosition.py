# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#
#         try:
#             return nums.index(target)
#         except ValueError:
#             length = len(nums)
#
#             i=0
#             while i <= length-1:
#                 if target==nums[i]:
#                     return i
#                 elif target<min(nums):
#                     return 0
#                 elif target>max(nums):
#                     return length
#                 elif target>nums[i]:
#                     i+=1
#                 elif target<nums[i]:
#                     return i
#             return i

######################################
# BOTH OF THE SOLUTIONS ARE ACCEPTED
######################################

from bisect import bisect

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        try:
            return nums.index(target)
        except ValueError:
            return bisect(nums, target)