class Solution:
    def minimumSteps(self, s: str) -> int:
        cntzero=s.count('0')
        print(cntzero)
        cntone=Counter()
        count=0
        for i in s:
            if i=='1':
                count+=(cntzero)
            else:
                cntzero-=1

        return count