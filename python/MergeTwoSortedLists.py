class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        l1 = list1
        l2 = list2

        if l1 == None :
            return l2
        if l2 == None :
            return l1
        
        dummy = ListNode()
        node = dummy

        while l1 != None and l2 != None :
            
            if l2.val <= l1.val:
                node.next=l2
                l2=l2.next
            else:
                node.next=l1
                l1=l1.next

            node = node.next

        if l1 != None:
            node.next=l1
        elif l2 != None:
            node.next=l2
        
        return dummy.next
