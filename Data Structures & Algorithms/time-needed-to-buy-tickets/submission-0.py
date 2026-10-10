
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:

        count = 0


        while True:

            for val,i in enumerate(tickets):
                if i > 0:
                    tickets[val] -= 1
                    count += 1
            
                if tickets[val] == 0 and val == k:
                    return count
                    
            
               
        
        
            
                
            
            
                

        
        





        