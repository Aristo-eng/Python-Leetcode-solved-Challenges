# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def print_elem(root):
    l=r=[]
    if root is None:
        return []
    l=print_elem(root.left)
    r=print_elem(root.right)  
    return l+[root.val]+r

class Solution(object):
    
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        elements = print_elem(root)

        curr = elements[0]
        
        for val in elements:
            if abs(target - val) < abs (target - curr):
                curr = val
        return curr
            
            
        