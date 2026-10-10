class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:


        maxval = 0
        curr = 0


        for i in range(len(nums)):
            if curr == 0:
                curr += nums[i]
                maxval = max(curr,maxval)
            
            else:
                if nums[i] > nums[i - 1]:
                    curr += nums[i]
                    maxval = max(curr,maxval)
                else:
                    curr = nums[i]
        
        return maxval
        