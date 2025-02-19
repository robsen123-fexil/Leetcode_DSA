class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        ordstrs=[0]*(len(s)+1)
        for a , b , c in shifts:
            if c==0:
                ordstrs[a]-=1
                ordstrs[b+1]+=1
            else:
                ordstrs[a]+=1
                ordstrs[b+1]-=1
        ordstrs=itertools.accumulate(ordstrs)  
        ans=""
        print(ordstrs)
        for a , b in zip(s , ordstrs):
           
            ans+=chr(((ord(a)+b)-97)%26+97)
        return ans



        