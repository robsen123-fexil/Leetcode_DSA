class UnionFind:
    def __init__(self, size):
        self.parent=[i for i in range(size) ]
        self.rank=[0 for i in range(size)]
    def find(self, x):
        while x!=self.parent[x]:
            self.parent[x]=self.parent[x]
            x=self.parent[x]
        return x
            
		
    def union(self, x, y):
        rtx=self.find(x)
        rty=self.find(y)
        if rtx==rty:
            return 
        if self.rank[rtx]<self.rank[rty]:
            self.parent[rtx]=rty
            self.rank[rty]+=1
            
        else:
            self.parent[rty]=rtx
            self.rank[rtx]+=1
                  
            
        
                
    def connected(self, x, y):
        return self.find(x) == self.find(x)
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        tree=UnionFind(len(isConnected))
        for i in range(len(isConnected)):
            for j in range(i+1 , len(isConnected)) :
                if isConnected[i][j]==1 and tree.find(i) != tree.find(j):
                    tree.union(i , j)
                    n-=1
        return n


                

















        # n = len(isConnected)             
        # visited = set()                   

        # def dfs(city):
        #     for neighbor in range(n):
        #         if isConnected[city][neighbor] == 1 and neighbor not in visited:
        #             visited.add(neighbor)
        #             dfs(neighbor)

        # provinces = 0

        # for city in range(n):
        #     if city not in visited:
        #         visited.add(city)
        
        #         dfs(city)
        #         provinces += 1            
        # return provinces