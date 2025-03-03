class Solution:
    def balancedStringSplit(self, s: str) -> int:
        sums=count=0
        for i in s:
            if i=='R':
                sums+=(-1)
            else:
                sums+=(1)
            if sums==0:
                count+=1
        return count