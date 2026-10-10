class Solution:
    from collections import Counter
    from collections import defaultdict
    def commonChars(self, words: List[str]) -> List[str]:

        prevCounter = None

        for i in words:
            myhash = defaultdict(int)
            currCounter = Counter(i)

            if prevCounter:
                for i in prevCounter:
                    if i in currCounter:
                        myhash[i] = min(prevCounter[i],currCounter[i])
                prevCounter = myhash
            if prevCounter == None:
                prevCounter = currCounter
        
        return(list(Counter(prevCounter).elements()))




            

        