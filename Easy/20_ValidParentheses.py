class Solution:
    def isValid(self, s: str) -> bool:
        
        #i is for [
        i=0
        #j is for {
        j=0
        #k is for (
        k=0
        
        s = s.replace("()", "")
        s = s.replace("[]", "")
        s = s.replace("{}", "")
        
        for letter in range(len(s)):
            
            if s[letter]=='[':
                i+=1
            elif s[letter]=='{':
                j+=1
            elif s[letter]=='(':
                k+=1
                
            elif s[letter]==']':
                if letter>0 and (s[letter-1]=='(' or s[letter-1]=='{'):
                    return False
                else:
                    i-=1
            elif s[letter]=='}':
                if letter>0 and (s[letter-1]=='(' or s[letter-1]=='['):
                    return False
                else:
                    j-=1
            elif s[letter]==')':
                if letter>0 and (s[letter-1]=='[' or s[letter-1]=='{'):
                    return False
                else:
                    k-=1

        if j==0 and i==0 and k==0:
            return True
        else:
            return False
