
class Solution(object):
    def preorderTraversal(self, root):
        def dfs(root):
            if not root:
                return []
            if not root.left and not root.right:
                return [root.val]

            return [root.val] + dfs(root.left) + dfs(root.right)

        return dfs(root)
