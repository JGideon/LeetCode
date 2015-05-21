class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    '''
    @param ListNode head
    @return ListNode
    '''
    def swapPairs(self, head):
        if head is None or head.next is None:
            return head
        dummyHead = ListNode(0)
        dummyHead.next = head
        pre = dummyHead
        while pre.next and pre.next.next:
            first = pre.next
            second = first.next
            
            pre.next = second
            first.next = second.next
            second.next = first
            
            first = second
            pre = second = first.next
            
        return dummyHead.next

#l1 = ListNode(1)
#l2 = ListNode(2)
#l3 = ListNode(3)
#l4 = ListNode(4)
#l1.next = l2
#l2.next = l3
#l3.next = l4
#s = Solution()
#resultList = s.swapPairs(l1)
#p = resultList
#while p:
#    print(p.val)
#    p = p.next

