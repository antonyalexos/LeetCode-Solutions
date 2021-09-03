# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.check(root,subRoot):return True
        if not root: return False
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
            
    def check(self,root,subroot):
        if not(root and subroot):
            return root is subroot
        return (root.val==subroot.val and self.check(root.left,subroot.left) and self.check(root.right,subroot.right))