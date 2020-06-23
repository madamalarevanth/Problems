# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
  
    def preorder(self,node,level,level_list):
        
        if node is None:
            return
        level_list.setdefault(level,[]).append(node.val)
        
        self.preorder(node.left,level+1,level_list)
        self.preorder(node.right,level+1,level_list)
        
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        level_dict={}
        
        self.preorder(root,0,level_dict)
        
        final_list=[]
        
        for i in range(len(level_dict)):
            final_list.append(level_dict[i])

        return final_list
        
        
    
