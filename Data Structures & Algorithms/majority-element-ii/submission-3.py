class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1, cand2 = None, None
        cnt1, cnt2 = 0, 0

        for num in nums:
            if cand1 == num:
                cnt1 += 1
            elif cand2 == num:
                cnt2 += 1
            elif cnt1 == 0:
                cand1, cnt1 = num, 1
            elif cnt2 == 0:
                cand2, cnt2 = num, 1
            else:
                cnt2 -= 1
                cnt1 -= 1
        
        n = len(nums)
        res = []
        for cand in (cand1, cand2):
            if cand is not None and nums.count(cand) > n // 3:
                res.append(cand)
        
        return res