class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []

        used = [False] * len(nums)
        nums.sort()

        def back(path):
            if len(path) == len(nums):
                res.append(path.copy())
                return 

            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                if used[i]:
                    continue
                
                used[i] = True
                
                path.append(nums[i])
                back(path)
                path.pop()
                used[i] = False
        
        back([])

        return res