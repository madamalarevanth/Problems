# This function returns the leftmost child of   
# nodes at the same level as p. This function  
# is used to getNExt right of p's right child  
# If right child of is None then this can also 
# be used for the left child
def getNextRight(root):
    temp = root.nextRight
    
    # Traverse nodes at root's level and find  
    # and return the next node's first child
    while(temp != None):
        if(temp.left):
            return temp.left
        elif(temp.right):
            return temp.right
        temp = temp.nextRight
    
    return None       

def connect(root):

    if (not root):
        return
    # Set nextRight for root  
    root.nextRight = None
    
    # set nextRight of all levels one by one
    while(root != None):
        q= root
        
        # Connect all childrem nodes of root and  
        # children nodes of all other nodes  
        # at same level as root
        while(q != None):
            # Set the nextRight pointer for  
            # root's left child
            if(q.left):
                #if right child of q exists 
                #then q.left.nextRight will be q.right
                if(q.right):
                    q.left.nextRight = q.right
                else:
                    q.left.nextRight = getNextRight(q)
                
            if (q.right): 
                q.right.nextRight = getNextRight(q)

            # Set nextRight for other nodes in 
            # pre order fashion
            q= q.nextRight
        
        if (root.left): 
            root = root.left  
        elif (root.right): 
            root = root.right  
        else: 
            root = getNextRight(root)
