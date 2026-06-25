class Solution:
    def isPalindrome(self, x: int) -> bool:
        orgnl = x
        mul_10 = x % 10
        if mul_10 == 0 and x != 0 or x < 0:
            return False
        work = orgnl
        rvrs = 0
        while work > rvrs:
            last_work = work % 10
            rvrs = rvrs * 10 + last_work
            work = work // 10
        return work == rvrs or work == rvrs // 10