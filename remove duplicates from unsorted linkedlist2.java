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
//without using buffer

class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if(head== null)
            return null;
        
        ListNode current=head.next;
        ListNode prev= head;
        
        
        while(current!= null)
        {
            ListNode runner = head;
            
            while(runner!=current)
            {
                if(runner.val == current.val)
                {
                    ListNode temp = current.next;
                    prev.next= temp;
                    current = temp;
                    break;
                }
                runner= runner.next;
            }
            if(current==runner)
            {
                prev= current;
                current= current.next;
            }
        }
        
        return head;
    }
}
