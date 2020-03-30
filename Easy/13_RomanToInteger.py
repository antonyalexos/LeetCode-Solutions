class Solution:
    def romanToInt(self, s: str) -> int:
        reversed_string = s[::-1]
        length = len(reversed_string)

        sum = 0
        dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        for i in range(length):
            if(i==0):
                sum += dict[reversed_string[i]]
            else:
                if(dict[reversed_string[i]] < dict[reversed_string[i-1]]):
                    sum -= dict[reversed_string[i]]
                else:
                    sum += dict[reversed_string[i]]
        return(sum)