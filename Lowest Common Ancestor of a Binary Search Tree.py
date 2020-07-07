# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def recursion(current_node):
            
            #reached end 
            if not current_node:
                return False
            
            #traverse left subtree
            left = recursion(current_node.left)
            
            #traverse right sub tree
            right = recursion(current_node.right)
            
            #mid variable is set to positive if current node is one of the required nodes
            mid = current_node==p or current_node==q
            
            #if more than two happens only when both nodes are found and they 
            #have reached a common point i.e common node  
            if mid+left+right>=2:
                self.ans = current_node
            
            return mid or left or right
        
        recursion(root)
        return self.ans
