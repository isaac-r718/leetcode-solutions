class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        ans = nums
        nums = nums[::-1]
        for i in range(len(nums)):
            ans.append(nums[i])
        return ans