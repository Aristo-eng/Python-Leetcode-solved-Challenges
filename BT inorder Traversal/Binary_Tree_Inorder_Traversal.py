# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]

        """
        l=r=[]
        if root is None:
            return []

        l=self.inorderTraversal(root.left)
        r=self.inorderTraversal(root.right)  
        return l+[root.val]+r


        
                    