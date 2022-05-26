# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
       
    
        array1 = []
        word1 = ""
        number1 = 0

        while l1 != None:
            array1.insert(0,l1.val)
            l1 = l1.next

        
        for i in array1:
            word1 += str(i)
            
        number1 = int(word1)    
        
        array2 = []
        word2 = ""
        number2 = 0
        
        while l2 != None:
            array2.insert(0,l2.val)
            l2 = l2.next

        for i in array2:
            word2 += str(i)
            
        number2 = int(word2)  
        
        number3 = number1 + number2
        
        array3 = []
        
        while number3 >= 10:
            array3.append(number3%10)
            number3 /= 10
        
        array3.append(number3)
        
        answer = ListNode()
        answer2 = answer
        answer.next = ListNode(3)
        answer = answer.next
        
        answer = ListNode(0)
        answer2 = answer
        
        for i in array3:
            answer.next = ListNode(i)
            answer = answer.next
            
        answer2 = answer2.next
        
            
        return answer2