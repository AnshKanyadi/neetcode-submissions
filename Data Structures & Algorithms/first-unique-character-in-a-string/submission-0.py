class Solution:
    from collections import Counter
    def firstUniqChar(self, s: str) -> int:
        s = list(s)
        mycounter = Counter(s)

        for i in range(len(s)):
            if mycounter[s[i]] == 1:
                return i 
        
        return -1 



    

    
        