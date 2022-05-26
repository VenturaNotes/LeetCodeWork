class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    
        #Brute force method is disgusting
      
        number1 = 0
        number2 = 0
        
        array = []
        count = 0
        countTracker = 0
        
        while count < len(s):
            if s[count] not in array:
                array.append(s[count])
                number1 +=1
                count+=1
            else:
                countTracker += 1
                count = countTracker
                array.clear()
                number1 = 0
            if number1 > number2:
                number2 = number1
        
        return number2
        