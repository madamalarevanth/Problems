# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def helper(t1,t2):
            if t1== None and t2== None :
                return True
            if t1== None or t1== None:
                return False
            return (t1.val==t2.val) and helper(t1.left,t2.right) and helper(t1.right,t2.left)
        return helper(root,root)
            
