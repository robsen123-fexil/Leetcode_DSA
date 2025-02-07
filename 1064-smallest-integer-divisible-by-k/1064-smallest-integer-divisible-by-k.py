class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        rm=1
        cnt=1
        if k%2==0 or k%5==0:
            return -1



        intial=rm%k
        while intial:
            intial=(intial*10+1)%k
            cnt+=1
        if intial==0:
            return int(cnt)
        return -1 

