LinkedListNode FindBeginning(ListNode head) {
  ListNode fast= head;
  ListNode slow = head;

  //finding loop using hare and tortoise 
  while(fast.next!=null)
  {
    slow=slow.next;
    fast=fast.next.next;
    
    if(fast==slow)
      break;
  }
  
  //now fast and slow are at meeting point
  
  //reset slow to head
  slow =head;
  
  //now move both of the pointers at slow pace they will meet at the start of loop
  while(fast!=slow)
  {
    fast=fast.next;
    slow=slow.next;
  }
  return fast;
}
