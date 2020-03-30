class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        length = len(digits)
        string = ''
        
        final_list = []
        
        for i in range(length):
            string += str(digits[i])
        
        number = int(string)
        number += 1
        
        return [int(d) for d in str(number)]
        