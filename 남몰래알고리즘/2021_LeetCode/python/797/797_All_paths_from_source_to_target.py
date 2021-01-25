from copy import deepcopy
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        n=len(graph)-1
        answer=[]
        visited=[False for _ in range(n+1)]
        
        def DFS(now , path):
            if now==n:
                answer.append(path)
                return
            
            for nextNode in graph[now]:
                visited[nextNode]=True
                tmp=deepcopy(path)
                tmp.append(nextNode)
                DFS(nextNode, tmp)
                visited[nextNode]=False
        
        DFS(0, [0])
        return answer
        