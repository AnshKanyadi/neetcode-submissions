class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        
        f = [0] + flowerbed + [0]
        numofplacements = 0
        
        
        for i in range(1, len(f) - 1):
            
            if f[i - 1] == 0 and f[i] == 0 and f[i + 1] == 0:
                f[i] = 1  
                numofplacements += 1
                
                
                if numofplacements >= n:
                    return True
        
        return numofplacements >= n
                    
        