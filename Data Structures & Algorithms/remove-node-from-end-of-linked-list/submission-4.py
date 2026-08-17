# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None:
            return head
        if head.next == None:
            return None
        temp = head.next
        head.next = None
        while temp != None:
            end = temp.next 
            temp.next = head
            head = temp
            temp = end

        if n == 1:
            head = head.next
        else:
            temp = head
            count = 1
            while temp.next != None:
                if count+1 == n:
                    # print("removed here ", temp.val)
                    temp.next = temp.next.next
                # print("here ", temp.val)
                temp = temp.next
                count += 1
                if temp == None:
                    break

        if head == None or head.next == None :
            return head
        temp = head.next
        head.next = None
        while temp != None:
            end = temp.next 
            temp.next = head
            head = temp
            temp = end 
        return head