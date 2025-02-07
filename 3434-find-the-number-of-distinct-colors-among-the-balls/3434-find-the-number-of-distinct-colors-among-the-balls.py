class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        cntlist=Counter()
        cntque=defaultdict(int)
        result=[]
        for a , b in queries:
            if cntlist[a]:
                
                cntque[cntlist[a]]-=1
                if cntque[cntlist[a]]==0:
                    cntque.pop(cntlist[a])
            cntlist[a]=b
            cntque[b]+=1
            result.append(len(cntque))
        return result

 