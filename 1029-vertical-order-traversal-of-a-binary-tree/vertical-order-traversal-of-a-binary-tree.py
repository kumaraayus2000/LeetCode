# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        q = deque()
        nodes = []

        q.append((root,0,0))
        #nodes.append([0,0,root.val])

        while q:
            root, row, col = q.popleft()

            nodes.append([col,row,root.val])

            if root.left is not None:
                q.append((root.left,row+1,col-1))

            if root.right is not None:
                q.append((root.right,row+1,col+1))

        
        nodes.sort()
        prev_node = None
        result = []
        for col,row,val in nodes:
            if prev_node != col:
                result.append([])
                prev_node = col

            result[-1].append(val)

        return result
            


            
