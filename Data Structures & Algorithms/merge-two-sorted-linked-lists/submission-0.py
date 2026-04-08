# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3 = ListNode()
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        if list1.val < list2.val:
            list3.val = list1.val
            curr = list1.next
            two = list2
        else:
            list3.val = list2.val
            curr = list1
            two = list2.next

        output = list3

        while curr != None or two != None:
            if curr == None:
                x = ListNode(two.val, None)
                list3.next = x
                list3 = list3.next
                two = two.next
            elif two == None:
                x = ListNode(curr.val, None)
                list3.next = x
                list3 = list3.next
                curr = curr.next
            else:
                if curr.val < two.val:
                    x = ListNode(curr.val, None)
                    list3.next = x
                    list3 = list3.next
                    curr = curr.next
                else:
                    x = ListNode(two.val, None)
                    list3.next = x
                    list3 = list3.next
                    two = two.next
            
        return output
    