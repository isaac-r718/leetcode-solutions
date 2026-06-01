class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        
        n = 1
        k_2 = 1
        
        while n % k != 0:
            n = (n * 10 + 1) % k
            k_2 = k_2 + 1
            
        return k_2