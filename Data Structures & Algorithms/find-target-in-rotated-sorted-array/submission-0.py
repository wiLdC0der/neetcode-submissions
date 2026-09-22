class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums)-1

        while left < right:
            mid = (left+right)//2

            if nums[mid]>nums[right]:
                left = mid+1
            else:
                right = mid
        pivot = left


        def bs(left,right):
            while left <= right:
                mid = (left+right)//2

                if nums[mid]==target:
                    return mid
                elif nums[mid]>target:
                    right = mid-1
                else:
                    left = mid+1
            return -1
       
        result = bs(0,pivot-1)
        if result != -1:
            return result
        
        return bs(pivot,len(nums)-1)

        