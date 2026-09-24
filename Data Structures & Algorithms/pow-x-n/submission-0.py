class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            x = 1/x
            n = -n
        curr = 1
        z = x
        while n > 0:
            if n % 2 == 0:
                z *= z
                n /= 2
            else:
                curr *= z
                n -= 1
        return curr