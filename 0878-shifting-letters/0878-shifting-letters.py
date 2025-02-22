class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        ords=[ord(x) for x in s]
        ords.append(0)
        pref=[0]*(len(ords)+1)
        for i  , val in enumerate(shifts):
            pref[0]+=val
            pref[i+1]-=val
        pref=list(accumulate(pref))
        for i  , val in enumerate(ords):
            ords[i]+=(pref[i])
        ans=""
        for i in ords:
            ans+=(chr((i-97)%26+97))
        return ans[:-1]