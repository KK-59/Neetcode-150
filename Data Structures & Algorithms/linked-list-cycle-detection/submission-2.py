# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # hash map method

        # rec = {} # linked list -> frequency
        # if head == None:
        #     return False
        # while head != None:
        #     if head.next == None:
        #         return False
        #     if head in rec:
        #         print(rec)
        #         return True
        #     rec[head] = 1
        #     head = head.next
        # return False

        # fast and slow pointer method 

        if head == None:
            return False

        slow = head
        fast = head.next
        while fast != None:
            if fast == slow:
                return True
            slow = slow.next
            if fast.next == None:
                return False
            else:
                fast = fast.next.next
        return False


