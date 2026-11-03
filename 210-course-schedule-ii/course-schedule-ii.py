class Solution:

    def dfs(self,graph,state,res,idx):
        if state[idx] ==1:
            return False

        if state[idx] == 2:
            return True

        state[idx] = 1

        for x1 in graph[idx]:
            if not self.dfs(graph,state,res,x1):
                return False

        state[idx] = 2

        res.append(idx)

        return True


    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        
        graph = [[] for _ in range (numCourses)]

        state = [0] * numCourses

        for u,v in prerequisites:
            graph[u].append(v)

        res = []
        for num in range(numCourses):

            if not self.dfs(graph,state,res,num):
                return []


        return res