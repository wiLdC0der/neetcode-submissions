class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        opening = ["(","[","{"]
        for ch in s:

            if ch in opening:
                stack.append(ch)
            else:
                if not stack:
                    return False
                elif stack and stack[-1] == "(" and ch == ")":
                    stack.pop()
                elif stack and stack[-1] == "[" and ch == "]":
                    stack.pop()
                elif stack and stack[-1] == "{" and ch == "}":
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
         
        