class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        my_dict = {
            2:"abc",
            3:"def",
            4:"ghi",
            5:"jkl",
            6:"mno",
            7:"pqrs",
            8:"tuv",
            9:"wxyz"
        }
        result = []
        def backtrack(i,path):
            if i == len(digits):
                result.append(path)
                return
            
            letters = my_dict[int(digits[i])]
            
            for d in letters:
                path+=d
                backtrack(i+1,path)
                path = path[:-1]
        
        if not digits:
            return []


        backtrack(0,"")    
        return result

        