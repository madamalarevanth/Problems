class Node(): 
    def __init__(self): 
        self.data = None
        self.next = None
def  deleteNode(node):
    if node== None or node.next==None:
      print("Failure")
    
    tmp = node.next
    node.data=tmp.data
    node.next= tmp.next
    print("Done")
