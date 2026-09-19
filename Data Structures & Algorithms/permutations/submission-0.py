class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        result = []

        def backtrack(path,used):

            if len(path) == len(nums):
                result.append(path[:])
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                path.append(nums[i])
                used[i] = True

                backtrack(path,used)
                used[i] = False
                path.pop()
            

        
        backtrack([],[False] * len(nums))
        return result
            

        