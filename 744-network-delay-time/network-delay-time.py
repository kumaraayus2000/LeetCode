class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        edges = collections.defaultdict(list)

        minheap = [(0,k)]

        for u,v,w in times:
            edges[u].append((v,w))


        visit = set()

        t = 0

        while minheap:
            w1,n1 = heapq.heappop(minheap)

            if n1 in visit:
                continue

            visit.add(n1)
            t= max(t,w1)

            for n2,w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minheap,(w1+w2,n2))

        return t if len(visit)==n else -1
