class Solution:
    def arrangeCoins(self, n: int) -> int:
        filled = 0
        Stair = n
        for i in range(n):
            Stair -= (i+1)
            filled += 1
            if Stair <= (i+1):
                return filled