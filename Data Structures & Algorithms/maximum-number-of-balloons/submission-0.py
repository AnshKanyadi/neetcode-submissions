from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        mymap = Counter(text)
        ans = 0
        condition = True

        while condition:
            for i in "balloon":
                if mymap[i] > 0:
                    mymap[i] -= 1
                else:
                    condition = False 

            if condition:
                ans += 1
         
        
        return ans

                
            
                

            

        




        