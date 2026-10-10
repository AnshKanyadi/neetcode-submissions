from collections import Counter 
class Solution:
    def longestPalindrome(self, s: str) -> int:

        theCounter = Counter(s)

        theOne = False
        totalcount = 0


        for i in theCounter:

            while theCounter[i] >= 2:
                totalcount += 2
                theCounter[i] -= 2
            
            if not theOne and theCounter[i] == 1:
                theOne = True
        
        if theOne:
            totalcount += 1
        
        return totalcount


            



        
        