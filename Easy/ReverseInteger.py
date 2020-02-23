class Solution:
    def reverse(self, x: int) -> int:
        
        def rev(x, p=0):
            if x<10:
                return p+x
            else:
                p = p*10+x%10 * 10
                return(rev(x//10,p))
           
        if(abs(rev(abs(x))) > (2 << 31 - 1)):
            return 0
        elif(x<0):
            return -rev(-x)
        else:
            return rev(x)
        