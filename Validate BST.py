# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    prev = None
    
    def isValidBST(self, root: TreeNode) -> bool:
        global prev 
        prev = None
        return self.isbst_rec(root)
    
    def isbst_rec(self,root): 
      
    # prev is a global variable 
        global prev  
  
    # if tree is empty return true 
        if root is None: 
            return True
  
        if self.isbst_rec(root.left) is False: 
            return False
  
        # if previous node'data is found  
        # greater than the current node's 
        # data return fals 
        if prev is not None and prev.val >= root.val: 
            return False
  
        # store the current node in prev 
        prev = root 
        return self.isbst_rec(root.right)
