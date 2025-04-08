class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color=[-1]*(len(graph))
        for i in range(len(graph)):
            if color[i]==-1:
                que=deque([i])
                color[i]=0
                while que:
                    nd=que.popleft()
                    for n in graph[nd]:
                        if color[n]==-1:
                            color[n]=1-color[nd]
                            que.append(n)
                        elif color[nd]==color[n]:
                            return False
        return True