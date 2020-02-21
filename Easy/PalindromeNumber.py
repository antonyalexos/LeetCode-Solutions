class Solution:

    def isPalindrome(self, x: int) -> bool:
        
        def rev(x, prod=0):
            if x < 10:
                return prod + x
            else:
                prod = prod * 10 + x%10 * 10
            return rev(x // 10, prod)
            
        if x<0:
            return False
        elif rev(x)==x:
            return True
        else:
            return False