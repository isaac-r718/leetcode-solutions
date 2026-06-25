class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2 or num == 4:
            return True
        x = num // 3
        while x * x > num:
            x = (x + num // x) // 2
        return x * x == num