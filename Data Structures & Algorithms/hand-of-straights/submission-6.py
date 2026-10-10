class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand = sorted(hand)
        rec = {} # number -> number of occurences in hand
        for i in range(len(hand)):
            if hand[i] in rec:
                rec[hand[i]] += 1
            else:
                rec[hand[i]] = 1
        # print(rec)
        total = 0
        for key in rec:
            total += rec[key]
        print(total)

        i = hand[0]
        counter = 0
        while total > 0:
            # print(i)
            # print("counter: ", counter)
            if i in rec and rec[i] > 0:
                total -= 1
                counter += 1
                rec[i] -= 1
                if counter == groupSize: 
                    counter = 0
                    if total > 0:
                        for key in rec: 
                            if rec[key] > 0:
                                i = key
                                break
                else:
                    i += 1
            else:
                break
        # print("count: ", counter)
        if counter == 0:
            return True
        else:
            return False



