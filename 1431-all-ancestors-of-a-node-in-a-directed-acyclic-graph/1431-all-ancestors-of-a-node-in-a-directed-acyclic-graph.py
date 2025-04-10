class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph=defaultdict(list)
        for src , dst in edges:
            graph[dst].append(src)
        result=[]
        for node in range(n):
            visited=set()
            que=deque(graph[node])
            while que:
                cur=que.popleft()
                if cur not in visited:
                    visited.add(cur)
                    que.extend(graph[cur])
            result.append(sorted(list(visited)))
        return result