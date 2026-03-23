# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
     #use stacks 2 
        if not root:
            return []

        s1 = [root]
        s2 = []
        ans = []

        while s1 or s2:
            level = []

            while s1:
                node = s1.pop()
                level.append(node.val)

                if node.left:
                    s2.append(node.left)
                if node.right:
                    s2.append(node.right)

            if level:
                ans.append(level)

            level = []

            while s2:
                node = s2.pop()
                level.append(node.val)

                if node.right:
                    s1.append(node.right)
                if node.left:
                    s1.append(node.left)

            if level:
                ans.append(level)
        
        return ans
        
        