class Solution:
    '''
    @param ListNode l1
    @param ListNode l2
    @return ListNode
    '''
    def mergeTwoLists(self, l1, l2):
        dummyHead = ListNode(0)
        p = l1
        q = l2
        newList = dummyHead
        while p and q:
            if p.val <= q.val:
               newList.next = p
               p = p.next 
               newList = newList.next
            else:
                newList.next = q
                q = q.next
                newList = newList.next
        if p:
            newList.next = p
        if q:
            newList.next = q
        return dummyHead.next

