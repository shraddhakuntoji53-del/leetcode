class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        from collections import defaultdict
        import math
        
        graph = defaultdict(list)
        
        # Build adjacency list
        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)
        
        self.fuel = 0
        
        def dfs(city, parent):
            # Each city has 1 representative
            people = 1
            
            for nei in graph[city]:
                if nei != parent:
                    people += dfs(nei, city)
            
            # Capital city does not need to travel upward
            if city != 0:
                self.fuel += math.ceil(people / seats)
            
            return people
        
        dfs(0, -1)
        return self.fuel
