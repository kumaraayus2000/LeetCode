# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def height(self,root: Optional[TreeNode])->int:
        if root is None:
            return 0
        
        l1 = 1 + self.height(root.left)
        l2 = 1 + self.height(root.right)

        return max(l1,l2)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        return self.height(root)
        
        