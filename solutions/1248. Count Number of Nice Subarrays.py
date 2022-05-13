class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        # 依然是同样的思路
        # 发现无法满足 sliding window的条件 
        # 加constraint
        
        # <= 2 - <= 1
        # nums = [2,1,2,1,2]
        # 1 + 2 + 3 + 4 + 5 - (1 + 2 + 3 + 2 + 3) = 15 - 11 = 4
        
        # Return the number of sub-arrays where there are less or equal tan k odd numbers on it
        def helper(nums, k):
            l = 0
            res = 0
            window_cnt = 0
            for r, val in enumerate(nums):
                if val % 2:
                    window_cnt += 1
                
                while window_cnt > k:
                    if nums[l] % 2:
                        window_cnt -= 1
                    l += 1
                
                res += r - l + 1
            return res
    
        return helper(nums, k) - helper(nums, k - 1)
