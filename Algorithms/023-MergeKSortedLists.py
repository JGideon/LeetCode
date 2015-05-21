class Solution:
    '''
    @param ListNode[] lists
    @return ListNode
    '''
    def mergeKLists(self, lists):
        originList = finalList = lists[0]
        for nodeList in lists:
            if originList is nodeList:
                continue
            i, j = 0, 0
            while i < len(finalList) and j < len(nodeList):
                
            
