class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # nums.sort()
        res = []
        def back(start, path):
            res.append(path.copy())
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                back(i + 1, path)
                path.pop()
        
        back(0, [])
        return res