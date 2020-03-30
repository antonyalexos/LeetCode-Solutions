class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs)==0:
            return ""
        elif len(strs)==1:
            return(strs[0])
        else:
            minimum_word = min(strs, key=len)
            length = len(min(strs, key=len))

            max_prefix = ""
            for i in range(1,length+1):
                result = all(word[:i] == minimum_word[:i] for word in strs)

                if(result):
                    max_prefix = minimum_word[:i]
            return max_prefix