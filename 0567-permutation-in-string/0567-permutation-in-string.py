class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        frst=s2[:len(s1)]
        if sorted(frst)==sorted(s1):
            return True
        l=0
        frst=list(frst)
        for i in range(len(s1) , len(s2)):
            frst.append(s2[i])
            frst.remove(s2[l])
            l+=1
            if sorted(''.join(frst))==sorted(s1):
                return True
        return False

            

