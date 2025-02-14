class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=maxima=0
        cnt=Counter()
        for i in range(len(s)):
            cnt[s[i]]+=1
            while (i-l+1)-max(cnt.values())>k:
                cnt[s[l]]-=1
                if cnt[s[l]]==0:
                    del cnt[s[l]]
                l+=1
            maxima=max(maxima , i-l+1)
        return maxima

