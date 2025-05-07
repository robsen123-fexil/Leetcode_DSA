class Solution:
    def equationsPossible(self, equations):
        parent = [i for i in range(26)]
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            parent[find(x)] = find(y)
        for i in equations:
            if '==' in i:
                x = ord(i[0]) - ord('a')
                y = ord(i[-1]) - ord('a')
                union(x, y)
        for i in equations:
            if '!=' in i:
                x = ord(i[0]) - ord('a')
                y = ord(i[3]) - ord('a')
                if find(x) == find(y):
                    return False

        return True
