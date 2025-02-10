class Solution:
    def frequencySort(self, s: str) -> str:
        cnt=Counter(s)
        srt=dict(sorted(cnt.items() , key=lambda x:(x[1] , x[0] ),reverse=True))
        ans=""
        for k , v in srt.items():
            ans+=''.join(k*v)
        return ans
        