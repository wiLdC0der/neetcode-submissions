class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        first = sorted(s1)
        length = len(s1)
        l = 0
        

        while l <= len(s2)-len(s1):
            substring = s2[l:length]
            if first == sorted(substring):
                return True
            else:
                l+=1
                length+=1
        return False
        