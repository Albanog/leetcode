# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        dummy = ListNode(0, head)
        front = dummy
        back = dummy

        front = front.next

        while front:
            front = front.next
            back = back.next
            if front:
                aux = back.val
                back.val = front.val
                front.val = aux
                front = front.next
                back = back.next

        return dummy.next