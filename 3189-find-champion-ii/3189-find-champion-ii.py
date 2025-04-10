class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegree=[0]*(n)
        for a , b in edges:
            indegree[b]+=1
        print(indegree)
        cnt=indegree.count(0)
        if cnt>=2:
            return -1
    
        for i , val in enumerate(indegree):
            if val==0:
                return i
        