class Solution:
    def isUgly(self, n: int) -> bool:

        num = n
        for factor in [2,3,5]:
            while (n % factor) == 0:
                n = n//factor
            
        
        return n== 1
            

        


        
