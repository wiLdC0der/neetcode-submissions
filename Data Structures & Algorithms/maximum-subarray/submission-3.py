class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) <=1:
            return nums[0]
        
        maximum = nums[0]
        total = 0
        for r in range(len(nums)):
            total+=nums[r]
            maximum = max(maximum,total)

            if total <= 0:
                total = 0
                
        return maximum
        




