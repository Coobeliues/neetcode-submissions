class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        rob1, rob2 = 0, 0
        for i in range(len(nums) - 1):
            temp = max(nums[i] + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        
        first, second = 0, 0
        for i in range(1, len(nums)):
            temp = max(nums[i] + first, second)
            first = second
            second = temp
        
        return max(rob2, second)