class Solution:

    def dfs(self, node):
        if node is None:
            return 0, 0

        left_sum, left_count = self.dfs(node.left)
        right_sum, right_count = self.dfs(node.right)

        total_sum = left_sum + right_sum + node.val
        total_count = left_count + right_count + 1

        if total_sum // total_count == node.val:
            self.ans += 1

        return total_sum, total_count


    def averageOfSubtree(self, root: TreeNode) -> int:
        self.ans = 0

        self.dfs(root)

        return self.ans