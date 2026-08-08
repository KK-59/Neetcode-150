class Solution:
    # def binSearch(self, hand:List[int], target:int) -> int:
    #     #binary search
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
                print("in here???")
                print("new removed: ",hand[goal])
                hand.pop(goal)
                goal = 0
                size = 1
                if len(hand) == 0:
                    return True
            if hand[goal]+1 not in hand:
                print("in here")
                print(hand[goal])
                print(hand)
                return False
            else:
                print("removed: ",hand[goal])
                print(hand)
                oldGoal = hand[goal]
                hand.pop(goal)
                goal = hand.index(oldGoal+1)
                
                print("new goal: ",goal)
                size += 1
            
        return True
