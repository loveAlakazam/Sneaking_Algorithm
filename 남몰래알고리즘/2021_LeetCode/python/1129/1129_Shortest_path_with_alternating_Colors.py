class Solution:
    
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        INF=float('inf')
        graph=[[] for _ in range(n)]
        d=[INF for _ in range(n)]
        
        #red(-1)
        for start, end in red_edges:
            graph[start].append((end, -1)) 
            
        #blue(1)
        for start,end in blue_edges:
            graph[start].append((end, 1))
        
        q=deque()
        
        def bfs(graph, start ,d):
            d[0]=0
            q.append((start, 0, 0)) #no color
            visited={}
            visited[(start, -1)]=True
            visited[(start, 1)]=True
            
            while q:
                now, w ,color=q.popleft()
                for neighbor in graph[now]:
                    if color==0 or color!=neighbor[1]:
                        if neighbor not in visited:
                            q.append((neighbor[0], w+1, neighbor[1] ))
                            visited[neighbor]=True
                            d[neighbor[0]]=min(d[neighbor[0]], w+1)
            
        bfs(graph, 0, d)
        d=[-1 if val==INF else val for val in d]
        return d