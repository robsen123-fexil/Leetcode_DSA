class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        result=[]
        safe={}
        def dfs(i):
            if i in safe:
                return safe[i]
            safe[i]=False
            for nei in graph[i]:
                if not dfs(nei):
                    return False
            safe[i]=True
            return True 
        for i in range(len(graph)):
            if dfs(i):
                result.append(i)
        return result