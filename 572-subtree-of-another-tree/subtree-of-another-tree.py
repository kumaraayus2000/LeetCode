# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isSubtree1(self,root,root1)-> bool:
        if root is None and root1 is None:
            return True

        if root is None or root1 is None:
            return False

        if root.val != root1.val:
            return False

        return (self.isSubtree1(root.left,root1.left) and
        self.isSubtree1(root.right,root1.right))

    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:

        if root is None:
            return False

        if self.isSubtree1(root,subRoot):
            return True

        return (self.isSubtree(root.left,subRoot) or 
        self.isSubtree(root.right,subRoot))      