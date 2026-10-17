class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        suma = 0
        for i in range(len(nums)):
            if nums[i] % 3:
                suma += 1
        return suma