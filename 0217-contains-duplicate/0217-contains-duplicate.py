class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        
        #1,2,3,1
        #What would be a better solution? 
        #Perhaps I should just check something else?
        
        def merge_sort(arr):
            if len(arr) > 1:
                left_arr = arr[:len(arr)//2]
                right_arr = arr[len(arr)//2:]
                
                merge_sort(left_arr)
                merge_sort(right_arr)
                
                i = j = k = 0
                
                while i < len(left_arr) and j < len(right_arr):
                    if left_arr[i] < right_arr[j]:
                        arr[k] = left_arr[i]
                        i+=1
                    else:
                        arr[k] = right_arr[j]
                        j+=1
                    k += 1
                        
                while i < len(left_arr):
                    arr[k] = left_arr[i]
                    i+=1
                    k+=1
                
                while j < len(right_arr):
                    arr[k] = right_arr[j]
                    j+=1
                    k+=1
        
        merge_sort(nums)
        for i in range(len(nums)):
            if i < len(nums) - 1:
                if nums[i] == nums[i+1]:
                    return True
        return False
            
 
        