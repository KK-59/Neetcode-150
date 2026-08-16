# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        pointer = head
        stack = []
        count = 0
        temp = head
        fillStack = head
        while temp != None:
            count += 1
            temp = temp.next
        # print(count)
        if count % 2 == 0:
            index = count // 2
        else:
            index = (count - 1) // 2
        # print(index)
        tempCount = -1
        if count % 2 != 0:
            while fillStack != None:
                tempCount += 1
                if tempCount > index:
                    tempFS = fillStack.next 
                    fillStack.next = None
                    stack.append(fillStack)
                    fillStack = tempFS
                else:
                    fillStack = fillStack.next
            while len(stack) > 0:
                tempCount += 2
                tempS = head.next
                pops = stack.pop()
                # print("stack: ", stack)
                # print(len(stack))
                head.next = pops
                pops.next = tempS
                head = tempS
            head.next = None
        else:
            while fillStack != None:
                tempCount += 1
                if tempCount >= index:
                    tempFS = fillStack.next 
                    fillStack.next = None
                    stack.append(fillStack)
                    fillStack = tempFS
                else:
                    fillStack = fillStack.next
            while len(stack) > 0:
                tempCount += 2
                tempS = head.next
                pops = stack.pop()
                # print("stack: ", stack)
                # print(len(stack))
                head.next = pops
                pops.next = tempS
                head = tempS
            head.next = None
        
        

        