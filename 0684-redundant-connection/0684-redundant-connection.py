class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents=[i for i in range(len(edges)+1)]

        def find(x):
            if parents[x]==x:
                return parents[x]
            parents[x]=find(parents[x])
            return parents[x]
        def uni(x , y):
            rtx=find(x)
            rty=find(y)
            if rtx==rty:
                return True
            parents[rty]=rtx
            return False
        for i , j in edges:
            if uni(i , j):
                return [i , j]
            
       