class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result=[]
        l=0
        frst=s[:len(p)]

        if sorted(frst)==sorted(p):
            result.append(0)
        frst=list(frst)
        for i in range(len(p) , len(s)):
            frst.append(s[i])
            frst.remove(s[l])
            
            if sorted(''.join(frst))==sorted(p):
                result.append(l+1)
            l+=1
        return result

