# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
         
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        resto = 0

        iterator1 = l1
        iterator2 = l2

        head = ListNode(0)
        l3 = head

        while iterator1 is not None and iterator2 is not None :
            aux = iterator1.val + iterator2.val + resto
            if aux > 9 :
                aux -=10
                l3.next=ListNode(aux)
                resto=1
            else:
                l3.next=ListNode(aux)
                resto=0

            iterator1 = iterator1.next
            iterator2 = iterator2.next
            l3 = l3.next

        if iterator1 is not None :
            while iterator1 is not None:
                aux = iterator1.val + resto
                if aux > 9 :
                    aux -=10
                    l3.next=ListNode(aux)
                    resto=1
                else:
                    l3.next=ListNode(aux)
                    resto=0

                iterator1 = iterator1.next
                l3 = l3.next

        else:
            while iterator2 is not None :
                aux = iterator2.val + resto
                if aux > 9 :
                    aux -=10
                    l3.next=ListNode(aux)
                    resto=1
                else:
                    l3.next=ListNode(aux)
                    resto=0

                iterator2 = iterator2.next
                l3 = l3.next

        if resto == 1:
            l3.next=ListNode(resto)
            
        return head.next