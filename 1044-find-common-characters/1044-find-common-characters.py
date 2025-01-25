class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        hsh={}
        for i in words:
            cnt=Counter(i)
            for k , v in cnt.items():
                if k not in hsh:
                    hsh[k]=v
                else:
                    hsh[k]=min(hsh[k] , v)
        rl=Counter()
        for i in words:
            wr=''.join(set(i))
            print(wr)
            for j in wr:
                rl[j]+=1
        print(hsh)
        result=[]
        for k , v in rl.items():
            if v==len(words):
                
                val=hsh[k]
                for i in range(val):
                    result.append(k)
        return result
        
    