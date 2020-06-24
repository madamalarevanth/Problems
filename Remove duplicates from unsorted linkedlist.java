/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
 
 // using buffer 
 
import java.util.Hashtable;
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        Hashtable table = new Hashtable();
        ListNode prev = null;
        ListNode n= head;
        
        while(n!=null)
        {
            if(table.containsKey(n.val))
                prev.next = n.next;
            else
            {
                table.put(n.val,true);
                    prev= n; 
            }
            n= n.next;
        }
        return head;
        
    }
}
