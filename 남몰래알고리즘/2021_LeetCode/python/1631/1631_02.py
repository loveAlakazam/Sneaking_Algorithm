# DFS인줄알고 시도하다가 실패함 ㅠㅠ;
class Solution:
    def __init__(self):
        self.answer = float('inf')

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])

        dy = [-1, 1, 0, 0]
        dx = [0, 0, -1, 1]
        visited = [[False]*cols for _ in range(rows)]

        def dfs(y, x, diff):
            if y == rows-1 and x == cols-1:
                self.answer = min(self.answer, diff)
                return

            for i in range(4):
                nexty = y+dy[i]
                nextx = x+dx[i]

                if (nexty >= 0 and nexty < rows) and (nextx >= 0 and nextx < cols):
                    if not visited[nexty][nextx]:
                        nextDiff = abs(heights[nexty][nextx]-heights[y][x])
                        if nextDiff >= diff:
                            nextDiff = max(nextDiff, diff)
                            visited[nexty][nextx] = True
                            dfs(nexty, nextx, nextDiff)
                            visited[nexty][nextx] = False

        visited[0][0] = True
        dfs(0, 0, 0)
        return self.answer
