class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        n = len(nums) // 2
        for i, cnt in d.items():
            if cnt > n:
                return i