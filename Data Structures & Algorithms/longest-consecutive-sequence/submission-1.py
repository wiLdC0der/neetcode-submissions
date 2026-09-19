class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        seen = set(nums)

        result = 0

        for num in nums:
            if num - 1 not in seen:
                count = 1
            
                while num + 1 in seen:
                    num+=1
                    count+=1
                result = max(result,count)

        return result

        