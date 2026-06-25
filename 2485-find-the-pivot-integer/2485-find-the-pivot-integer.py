class Solution:
    def pivotInteger(self, n: int) -> int:
        sum_total = (n*(n+1))/2
        x = sum_total ** (1/2)
        if int(x) == x:
            return int(x)
        else:
            return -1