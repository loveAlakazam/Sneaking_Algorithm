class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows= len(heights)
        cols= len(heights[0])
        q=[]
        dy=[-1,1,0,0]
        dx=[0,0,-1,1]
        visited=[[False]*cols for _ in range(rows)]
        
        # 다익스트라 사용
        # 절대값의 차이값(effort)가 가장 작은것을 우선으로한다.
        def dijkstra():
            heapq.heappush(q, (0,0,0))
            
            while q:
                effort, nowy, nowx=heapq.heappop(q)
                if (nowy==rows-1) and(nowx==cols-1):
                    return effort
                
                if not visited[nowy][nowx]:
                    visited[nowy][nowx]=True
                    for i in range(4):
                        nexty=nowy+dy[i]
                        nextx=nowx+dx[i]
                        if (nexty>=0 and nexty<rows) and (nextx>=0 and nextx<cols):
                            if not visited[nexty][nextx]:
                                nextEffort= max( abs(heights[nexty][nextx]-heights[nowy][nowx]) , effort)
                                heapq.heappush(q,(nextEffort, nexty, nextx))

                
        result=dijkstra()
        return result