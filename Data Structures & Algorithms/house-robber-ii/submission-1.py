class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) <= 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])

        
        def dynamic(arr):
            dp = [0] * len(arr)

            dp[0] = arr[0]
            dp[1] = max(arr[1],dp[0])

            for i in range (2,len(arr)):
                dp[i] = max(dp[i-1],dp[i-2]+arr[i])
            
            return dp[-1]
        
        first = dynamic(nums[1:])
        second = dynamic(nums[:len(nums)-1])

        return max(first,second)
        