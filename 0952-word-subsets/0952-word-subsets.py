class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        w=words2[0]
        cw=Counter(w)
        hsh1={}
        for i in range(1 , len(words2)):
            cnt=Counter(words2[i])
            for k , v in cnt.items():
                if cw[k]:
                    cw[k]=max(v , cw[k])
                else:
                    cw[k]=v
        print(cw)
        result=[]
        for i in range(len(words1)):
            cnt2=Counter(words1[i])
            flg=True
            for k , v in cw.items():
                if cnt2[k] and cnt2[k]>=v:
                    continue
                else:
                    flg=False
                    break

            if flg:
                result.append(words1[i])
        return result
                
        