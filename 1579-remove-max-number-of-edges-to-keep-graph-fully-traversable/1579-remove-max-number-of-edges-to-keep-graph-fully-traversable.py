class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)
        self.components = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        self.components -= 1
        return True


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        dsuAlice = DSU(n)
        dsuBob = DSU(n)
        usedEdges = 0

        # Step 1: Type 3 edges
        for t, u, v in edges:
            if t == 3:
                if dsuAlice.union(u, v):
                    dsuBob.union(u, v)
                    usedEdges += 1

        # Step 2: Type 1 edges (Alice)
        for t, u, v in edges:
            if t == 1:
                if dsuAlice.union(u, v):
                    usedEdges += 1

        # Step 3: Type 2 edges (Bob)
        for t, u, v in edges:
            if t == 2:
                if dsuBob.union(u, v):
                    usedEdges += 1

        # Step 4: Connectivity check
        if dsuAlice.components > 1 or dsuBob.components > 1:
            return -1

        return len(edges) - usedEdges
