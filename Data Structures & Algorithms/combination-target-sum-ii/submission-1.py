class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()

        result = []

        def backtrack(i,path,total):
            if total == target:
                return result.append(path[:])
            
            if total > target or i == len(candidates):
                return
            
            path.append(candidates[i])

            backtrack(i+1,path,total+candidates[i])

            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            
            path.pop()
            backtrack(i+1,path,total)
        backtrack(0,[],0)
        return result
            

        