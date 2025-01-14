class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        result=[]
        a=[]
        b=[]
        for i , j in zip(A  , B):
            a.append(i)
            b.append(j)
            cnt1=Counter(a)
            cnt2=Counter(b)
            count=0
            for k , v in cnt1.items():
                if cnt2[k]:
                    count+=(cnt2[k])
            result.append(count)
        return result
