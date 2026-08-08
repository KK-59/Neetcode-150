class Solution:
    def binSearch(self, hand:List[int], target:int, l:int, r:int) -> int:
        if l > r - 1:
            return -1
        m = (r + l) // 2
        if hand[m] == target:
            return m
        if hand[m] > target:
            return self.binSearch(hand, target, l, m)
        else:
            return self.binSearch(hand, target, m+1, r)

        
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand = sorted(hand)
        if len(hand) % groupSize != 0:
            return False
        if groupSize == 1:
            return True
        # 1,2,2,3,3,4,4,5
        size = 1
        goal = 0
        while len(hand) > 0:
            if size == groupSize:
                # print("in here???")
                # print("new removed: ",hand[goal])
                hand.pop(goal)
                goal = 0
                size = 1
                if len(hand) == 0:
                    return True
            res = self.binSearch(hand, hand[goal]+1, 0, len(hand))
            if res == -1: 
                # hand[goal]+1 not in hand:
                # print("in here")
                # print(hand[goal])
                # print(hand)
                return False
            else:
                # print("removed: ",hand[goal])
                # print(hand)
                oldGoal = hand[goal]
                hand.pop(goal)
                goal = self.binSearch(hand,oldGoal+1,0,len(hand))
                # hand.index(oldGoal+1)
                
                print("new goal: ",goal)
                size += 1
            
        return True
