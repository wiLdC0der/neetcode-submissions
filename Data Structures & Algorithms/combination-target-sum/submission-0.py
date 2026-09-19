class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        result = []

        def backtrack(i,path,total):
            if total == target:
                return result.append(path[:])
            if total > target or i == len(nums):
                return
            
            path.append(nums[i])
            backtrack(i,path,total+nums[i])
 
            
            path.pop()

            backtrack(i+1,path,total)
        
        backtrack(0,[],0)
        return result

        