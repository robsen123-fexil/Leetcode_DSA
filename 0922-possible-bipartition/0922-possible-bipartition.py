class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph=defaultdict(list)
        color=[-1]*(n+1)
        for a , b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        color=[-1]*(n+1)
        for i in range(1 , n+1):
            if color[i]==-1:
                que=deque([i])
                color[i]=0
                while que:
                    nd= que.popleft()
                    for n in graph[nd]:
                        if color[n]==-1:
                            color[n]=1-color[nd]
                            que.append(n)
                        elif color[n]==color[nd]:
                            return False
        return True
