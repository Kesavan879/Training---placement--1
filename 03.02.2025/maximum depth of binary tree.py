
class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        leftheight=self.maxDepth(root.left)
        rightheight=self.maxDepth(root.right)
        return 1+max(leftheight,rightheight)    


        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
