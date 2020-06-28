/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
    //use hashmap to keep track of all the nodes added in the copy
    HashMap<Node,Node> hm = new HashMap<>();
    
    public Node cloneGraph(Node node) {
        
        if (node==null)
            return null;
        hm.put(node, new Node(node.val,new ArrayList<>()));
        
        for(Node neighbor: node.neighbors)
        {
            if(hm.containsKey(neighbor))
                //if the neighbor exists in hm => clone node also exist 
                //add the node neighbors to clone node 
                hm.get(node).neighbors.add(hm.get(neighbor));
            else
                //if the neighbor is not in the map then we didnt see it yet 
                //so we need to create a clone node for it and then add it.
                //call the recursive function clone graph which clones this node and adds it to map
                hm.get(node).neighbors.add(cloneGraph(neighbor));
        }
        //return the source node of the cloned graph 
        return hm.get(node);
    }
}
