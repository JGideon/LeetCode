#encoding=utf-8
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    '''
    @param ListNode head
    @param integer n
    @return ListNode
    '''
    def removeNthFromEnd(self, head, n):
        dummyHead = ListNode(0)
        dummyHead.next = head
        slow = quick = dummyHead.next
        for i in range(n):
            quick = quick.next
        while quick.next:
            slow = slow.next
            quick = quick.next
        slow.next = slow.next.next 
        return dummyHead.next
            
