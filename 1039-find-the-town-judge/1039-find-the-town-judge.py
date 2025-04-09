class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        cnt=defaultdict(int)
        count=defaultdict(int)
        for i in range(n):
            cnt[i+1]=-1
        for a , b in trust:
            cnt[a]+=1
            count[b]+=1
        for k , v in cnt.items():
            if v==-1 and count[k]==(n-1):
                return k
        return -1
