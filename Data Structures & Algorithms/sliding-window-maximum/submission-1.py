class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        a = []
        l, r = 0, k
        seen = set()

        while r <= len(nums):

            mx = max(nums[l:r])
            a.append(mx)
            l += 1
            r += 1
        return a