class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        result = []
        temp =[]

        def backtrack(openn,closee):
            if len(temp)== 2*n:
                result.append("".join(temp))
                return True

            
            if openn < n:
                temp.append("(")
                backtrack(openn+1,closee)
                temp.pop()
            
            if openn>closee:
                temp.append(")")
                backtrack(openn,closee+1)
                temp.pop()
        backtrack(0,0)
        return result
        