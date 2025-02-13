class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result=[]
        l=0
        frst=s[:len(p)]

        cnt1=Counter(p)
        cnt2=Counter(frst)
        if cnt1==cnt2:
            result.append(0)
        for i in range(len(p) , len(s)):
            cnt2[s[l]]-=1
            if cnt2[s[i]]==0:
                del cnt2[s[i]]
            cnt2[s[i]]+=1
            if cnt2==cnt1:
                result.append(l+1)
            l+=1
        return result

