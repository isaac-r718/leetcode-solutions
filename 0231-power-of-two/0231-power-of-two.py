class Solution:
    import math
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        log = math.log2(n)
        if log % 1 == 0:
            return True
        else:
            return False