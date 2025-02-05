class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        result=0
        def checker(s , t):
            cnt1=Counter(t)
            for i in s:
                if cnt1[i] and s.count(i)<=cnt1[i]:
                    continue
                else:
                    return False
            return True
        count=0
        for w in words:
            if checker(w , chars ):
                count+=len(w)
        return count