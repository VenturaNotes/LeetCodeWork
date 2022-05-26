class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        array = []
        for i in nums1:
            array.append(i)
        
        for i in nums2:
            array.append(i)
            
        array = sorted(array)
        if len(array) % 2 != 0:
            return array[int((len(array)-1)/2)]
        else:
            return((array[int(len(array)/2)-1] + array[int(len(array)/2)])/2)
            
 
   