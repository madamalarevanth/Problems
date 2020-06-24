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
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        if(head==null|| n<1)
            return null;
        //create two pointers 
        ListNode prev=head;
        ListNode p1= head;
        ListNode p2= head;
        
        
        //increment the pointer p2 by n-1
        for(int i=1;i<n;i++)
        {
           if(p2==null)
               return null;
        p2=p2.next;
        }
        
        while(p2.next !=null)
        {
            prev=p1;
            p1=p1.next;
            p2=p2.next;
        }
        
        //at the end the pointer p1 points at the nth node from the end of teh list
        if(p1==head)
            head=head.next;
        else
        {
            prev.next= p1.next;
        }
        
        return head;  
            
    }
}
