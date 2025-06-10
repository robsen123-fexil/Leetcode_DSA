from collections import Counter

class Solution(object):
    def maxDifference(self, s):
        cnt = Counter(s)
        eve =inf
        odd = -inf
        for v in cnt.values():
            if v % 2 == 0:
                eve = min(eve, v)
            else:
                odd = max(odd, v)
        return odd - eve