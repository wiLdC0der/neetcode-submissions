class Solution:
    def partition(self, s: str) -> List[List[str]]:

        result = []

        def backtrack(i,path):
            if  i == len(s):
            
                result.append(path[:])
                return
            
            for j in range(i,len(s)):
                substring = s[i:j+1]
                if substring == substring[::-1]:
                    path.append(substring)
                    backtrack(j+1,path)
                    path.pop()
            
        backtrack(0,[])
        return result