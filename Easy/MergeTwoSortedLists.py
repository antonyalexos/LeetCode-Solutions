# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        if l1==None and l2==None:
            return None
        
        elif l1!=None and l2!=None:
            if l1.val>=l2.val:
                array = ListNode(l2.val)
                head = array
                l2 = l2.next
            else:
                array = ListNode(l1.val)
                head = array
                l1 = l1.next
        elif l1==None and l2!=None:
            array = ListNode(l2.val)
            head = array
            l2 = l2.next
        elif l1!=None and l2==None:
            array = ListNode(l1.val)
            head = array
            l1 = l1.next
            
        while(l1!=None and l2!=None):
            if l1.val >= l2.val:
                array.next = ListNode(l2.val)
                array = array.next
                l2 = l2.next
            else:
                array.next = ListNode(l1.val)
                array = array.next
                l1 = l1.next
        
        while(l1==None and l2!=None):
            array.next = ListNode(l2.val)
            array = array.next
            l2 = l2.next
        
        while(l1!=None and l2==None):
            array.next = ListNode(l1.val)
            array = array.next
            l1 = l1.next
            
        return(head)
                     