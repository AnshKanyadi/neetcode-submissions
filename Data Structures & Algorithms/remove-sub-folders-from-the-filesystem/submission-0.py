class Solution:
    def removeSubfolders(self, folder: list[str]) -> list[str]:
        myset = set(folder)
        output = []
        #peter fuck the shit out of me
        
        for f in folder:
           
            parts = f.split('/')
            add = True
            
             
          
            for i in range(2, len(parts)):
                parent = '/'.join(parts[:i])
                if parent in myset:
                    add = False
                    break 
                    
            if add:
                output.append(f)
                
        return output