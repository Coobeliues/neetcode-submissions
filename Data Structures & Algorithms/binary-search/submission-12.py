import bisect

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # l, r = 0, len(nums) - 1
        
        # while l <= r:
        #     # mid = (r + l) // 2
        #     mid = l + (r - l) // 2
        #     if nums[mid] == target:
        #         return mid
        #     if nums[mid] > target:
        #         r = mid - 1
        #     elif nums[mid] < target:
        #         l = mid + 1
        # return -1


        # i = bisect.bisect_left(nums, target)
        i = bisect.bisect_right(nums, target)
        
        if i > 0 and nums[i - 1] == target:
            return i - 1

        # if i > len(nums) and nums[i] == target:
        #     return i

        
        return -1