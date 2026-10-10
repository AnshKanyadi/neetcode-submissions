class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if len(digits) == 0:
            return []
        
        digits = list(digits)
        def backtrack(curr,n):
            if len(curr) == len(digits):
                ans.append("".join(curr[:]))
                return

            for num in phone_keypad[digits[n]]:
                curr.append(num)
                backtrack(curr,n+1)
                curr.pop()

        ans = []

        
        phone_keypad = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"]
}

        backtrack([],0)
        return ans
        

        