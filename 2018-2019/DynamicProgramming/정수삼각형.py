def solution(triangle):
    triangle_row= len(triangle)
    
    for r in range(triangle_row-1,-1,-1):
        if r<triangle_row-1:
            for c in range(0,len(triangle[r])):
                now= triangle[r][c]
                triangle[r][c]= max(now+triangle[r+1][c], now+triangle[r+1][c+1])          
    return triangle[0][0]
