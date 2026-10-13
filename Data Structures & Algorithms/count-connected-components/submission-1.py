class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        count = 0
        seen = set()

        mymap = defaultdict(list)


        for x,y in edges:
            mymap[x].append(y)
            mymap[y].append(x)




        def dfs(val):
            for neighbor in mymap[val]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)
        
        for i in range(n):

            if i not in seen:
                seen.add(i)
                count += 1
                dfs(i)
        

        
        return count
            


        