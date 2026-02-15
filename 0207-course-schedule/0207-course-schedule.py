class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict
        
        graph = defaultdict(list)
        
        # Build graph
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        
        state = [0] * numCourses  # 0 = unvisited, 1 = visiting, 2 = visited
        
        def dfs(course):
            if state[course] == 1:
                return False  # cycle found
            if state[course] == 2:
                return True   # already processed
            
            state[course] = 1  # mark as visiting
            
            for next_course in graph[course]:
                if not dfs(next_course):
                    return False
            
            state[course] = 2  # mark as visited
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True
