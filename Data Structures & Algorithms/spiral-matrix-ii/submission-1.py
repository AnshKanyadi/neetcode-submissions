class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:


        left = 0
        right = n - 1
        top = 0
        down = n - 1


        matrix = [[0] * n for _ in range(n)]


        val = 1


        while left <= right and top <= down:

            for i in range(left,right + 1):
                matrix[top][i] = val
                val += 1
            
           
            top += 1

            for i in range(top,down + 1):
                matrix[i][right] = val
                val += 1
            
            right -= 1
            
            
           

            for i in range(right,left - 1,-1):
                matrix[down][i] = val
                val += 1
            
            down -= 1
            
            

            for i in range(down, top - 1, -1):
                matrix[i][left] = val
                val += 1
            
            left += 1
        
        return matrix 


                




        






        
        