/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        
        Stack<TreeNode> st = new Stack();
        
        st.push(root);
        
        //answer list
        List<Integer> ans = new LinkedList<Integer>();
            
        while(!st.isEmpty())
        {
            
            TreeNode node =st.pop();
            if(node!=null)
            {
                st.push(node.left);
                st.push(node.right);
                ans.add(node.val);
            }
        }
        
        return ans;
    }
}
