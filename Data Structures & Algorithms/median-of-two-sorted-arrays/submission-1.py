class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        i = 0
        j = 0

        result = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                result.append(nums1[i])
                i+=1
            else:
                result.append(nums2[j])
                j+=1
        while i < len(nums1):
            result.append(nums1[i])
            i+=1
        while j < len(nums2):
            result.append(nums2[j])
            j+=1

        mid = len(result) // 2
        if len(result) % 2 == 1:
            return float(result[mid])
        else:
            return (result[mid] + result[mid - 1]) / 2.0
                    