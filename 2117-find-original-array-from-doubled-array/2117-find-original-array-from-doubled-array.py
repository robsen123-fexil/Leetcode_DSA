class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        result=[]
        if len(changed)<=1:
            return []
        cnt=Counter(changed)
        for i in range(len(changed)):
            if cnt[changed[i]]>0:
                if cnt[changed[i]*2]>0:
                    cnt[changed[i]]-=1
                    cnt[changed[i]*2]-=1
                    result.append(changed[i])
                else:
                    return []
        return result

