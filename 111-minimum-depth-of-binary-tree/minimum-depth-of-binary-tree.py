# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minheight(self,root:Optional[TreeNode])->int:
        if root is None:
            return 0
        
        l1 =  self.minheight(root.left)
        r1 =  self.minheight(root.right)

        if root.left is None:
            return 1 + r1
        
        if root.right is None:
            return 1 + l1

        return 1 + min(l1,r1)

    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        return self.minheight(root)
