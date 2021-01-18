class Solution:
    subtrees ={}
    # Separator node
    MARKER = '$'
    
    def dupSubUtil(self,root):
        global subtrees
        s=""
        
        # If current node is None, return marker
        if (root == None):
            return s + MARKER
        
        # If left subtree has a duplicate subtree.
        lStr = self.dupSubUtil(root.left)
         
        if (s in lStr):
           return s
     
        # Do same for right subtree
        rStr = self.dupSubUtil(root.right)
         
        if (s in rStr):
           return s
     
        # Serialize current subtree
        s = s + root.key + lStr + rStr
            
      
        # If current subtree already exists in hash
        # table. [Note that size of a serialized tree
        # with single node is 3 as it has two marker nodes.
        if len(s)>3 and s in subtrees:
            return ""
        
        subtrees[s] = 1
        
        return s
        
    def dupSub(self, root):
        str = self.dupSubUtil(root)
        
        if "" in str:
            return True
        
        return False
