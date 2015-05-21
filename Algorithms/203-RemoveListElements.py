class Solution:
    def removeElements(self, head, val):
        dummyHead = ListNode(0)
        dummyHead.next = head
        preP = dummyHead
        p = preP.next
        while p:
            if p.val is val:
                preP.next = p.next
                p = p.next
            else:
                preP = preP.next
                p = p.next
        return dummyHead.next

