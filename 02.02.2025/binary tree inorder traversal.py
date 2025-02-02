
class Solution(object):
    def inorderTraversal(self, root):
        l=[]
        def inorder(root):
            if root == None:
                return 
            
            inorder(root.left)
            l.append(root.val)
            inorder(root.right)
        inorder(root)

        return l
