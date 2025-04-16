class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        q=deque()
        visit=set()
        res=[[-1]*len(isWater[0]) for _ in range(len(isWater))]
        
        for r in range(len(isWater)):
            for c in range(len(isWater[0])):
                if isWater[r][c]:
                    res[r][c]=0
                    q.append((r , c))
                    visit.add((r , c))
     
        while q:
            r,c=q.popleft()
            h=res[r][c]
            ng=[[r+1 , c] , [r , c+1] , [r-1 , c] , [r , c-1]]
            for nr , nc in ng:
                if (nr<0 or nc<0 or nc>=len(isWater[0] ) or nr>=len(isWater)) or (nr , nc) in visit:
                    continue

                q.append((nr , nc))
                visit.add((nr , nc))
                res[nr][nc]=h+1
        return res
        print(q)

              

        

