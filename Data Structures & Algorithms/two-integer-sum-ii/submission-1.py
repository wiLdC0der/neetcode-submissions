class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        r = 0
        l = len(numbers)-1

        while r < l:
            total = numbers[r] + numbers[l]

            if total == target:
                return [r+1,l+1]

            elif total > target:
                l-=1
            else:
                r+=1
        return [-1,-1]
        