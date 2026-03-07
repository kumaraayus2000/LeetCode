# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def inorder(self, root:Optional[TreeNode],v1: List[int]):
        if root is None:
            return

        self.inorder(root.left,v1)
        v1.append(root.val)
        self.inorder(root.right,v1)

        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        v1 = []

        self.inorder(root,v1)

        return v1[k-1]
        