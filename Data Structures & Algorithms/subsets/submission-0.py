class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result  = []

        def backtracking(i,path):
            if i == len(nums):
                return result.append(path[:])
                
            
            path.append(nums[i])
            backtracking(i+1,path)
            path.pop()
            backtracking(i+1,path)

        backtracking(0,[])
        return result