# Collaborators: Manasi Kulkarni and Paul Walters

class Solution:
    def romanToInt(self, s: str) -> int:
        legend = {"I": 1, "V": 5, "X":10, "L": 50, "C": 100, "D": 500, "M": 1000}
        
        output = 0
        prev = s[0]
        
        for num in s: 
            output += legend[num]
            if(legend[num]>legend[prev]):
                output = output-2*(legend[prev])

            prev=num
        return output