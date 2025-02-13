class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cnt=Counter()
        maxima=float('-inf')
        l=0
        if not s:
            return 0
        for i in range(len(s)):
            cnt[s[i]]+=1
            while cnt[s[i]]>=2:
                cnt[s[l]]-=1
                if cnt[s[l]]==0:
                    del cnt[s[l]]
                l+=1
            maxima=max(maxima , len(cnt))
        return maxima
