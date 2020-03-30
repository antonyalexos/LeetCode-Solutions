class Solution:
    def countAndSay(self, n: int) -> str:
        
        i=0
        final_string = '1'
        if n==1:
            return '1'
        
        while 1 < n:            
            string = ''
            
            length = len(final_string)
            for j in range(length):
                try:
                    if final_string[j]==final_string[j+1]:
                        i+=1
                    elif final_string[j]!=final_string[j+1]:
                        string += str(i+1)
                        string += final_string[j]
                        i=0
                        
                except IndexError:
                    string += str(i+1)
                    string += final_string[j]
                    i=0
            
            final_string = string 
            n -= 1
            
        return final_string
 