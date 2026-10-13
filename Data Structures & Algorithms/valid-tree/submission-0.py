from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:


        mymap = defaultdict(list)
        seen = {0}
        flag = True

        print("hello")

        for x,y in edges:
            mymap[x].append(y)
            mymap[y].append(x)

        

        def dfs(node,parent):
            nonlocal flag
           
            
            for neighbor in mymap[node]:
                if neighbor in seen and neighbor != parent:
                    flag = False
                   
                
                if neighbor not in seen:
                    
                    seen.add(neighbor)
                    dfs(neighbor,node)
                

            
          
        
        dfs(0,None)
        

        if not flag:
            return False
    
        for i in range(n):
            if i not in seen:
                return False
                
        
        return True 
        


                

            

            





        