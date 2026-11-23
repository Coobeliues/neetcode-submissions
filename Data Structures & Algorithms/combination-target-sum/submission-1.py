class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def back(start, path, total):
            if total == target:
                res.append(path.copy())
            
            for i in range(start, len(nums)):
                if total + nums[i] > target:
                    continue
                path.append(nums[i])
                back(i, path, total + nums[i])
                path.pop()
            
        back(0, [], 0)

        return res