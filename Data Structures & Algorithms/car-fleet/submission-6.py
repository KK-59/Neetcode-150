import math
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 0
        cars = []
        for i in range(len(position)): 
            cars.append((position[i], speed[i]))
        cars = sorted(cars, reverse=True)
        # print(cars)
        rec = []
        for i in range(len(cars)): 
            x = (target - cars[i][0]) / cars[i][1]
            rec.append(x)
            if len(rec) > 1 and rec[i] < rec[i-1]:
                rec[i] = rec[i-1]
        # print(rec)
        while len(rec) > 0: 
            fleets += 1
            x = rec.pop()
            while len(rec) > 0 and rec[-1] == x:
                rec.pop()
        return fleets



                

