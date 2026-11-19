class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mx_len = 0
        num_set = set(nums)

        for n in num_set:
            if (n - 1) not in num_set:
                length = 1
                while (n + length) in num_set:
                    length += 1
                mx_len = max(mx_len, length)
        
        return mx_len
