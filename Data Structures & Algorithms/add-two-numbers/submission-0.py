# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0,None)
        result = res
        carry = 0
        while l1 != None or l2 != None:
            dig1 = 0
            dig2 = 0
            if l1 == None:
                dig1 = 0
                dig2 = l2.val
            elif l2 == None:
                dig2 = 0
                dig1 = l1.val
            else:
                dig1 = l1.val
                dig2 = l2.val
            add = dig1 + dig2 + carry
            carry = 0
            if add < 10:
                res.next = ListNode(add, None)
            else:
                carry = 1
                add = add % 10
                res.next = ListNode(add, None)
            print(res.val)
            res = res.next
            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next
        if carry == 1:
            res.next = ListNode(1, None)
        return result.next