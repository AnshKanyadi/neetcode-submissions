from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        n = len(s)
        if max(counts.values()) > (n + 1) // 2:
            return ""

        res = [""] * n
        i = 0
        for ch, c in counts.most_common():
            for _ in range(c):
                res[i] = ch
                i += 2
                if i >= n:
                    i = 1
        return "".join(res)