class Solution:
    def mirrorDistance(self, n: int) -> int:
        n_reverse = str(n)[::-1] 
        return abs(n - int(n_reverse))