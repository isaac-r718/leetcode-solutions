class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            output.append(nums[i])
        for i in range(len(nums)):
            output.append(nums[i])
        return output
        