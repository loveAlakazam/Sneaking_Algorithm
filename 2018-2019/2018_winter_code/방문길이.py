# https://programmers.co.kr/learn/courses/30/lessons/49994?language=python3#
def solution(dirs):
    #문자열을 리스트로 나타낸다.
    dirs=list(dirs)
    # 출발지
    sta_x, sta_y= 0,0
    
    # 목적지: 
    end_x, end_y=0,0
    arrows=[]    
    for di in dirs:
        if di is 'L':
            end_x=sta_x-1
        elif di is 'R':
            end_x=sta_x+1
        
        if di is 'U':
            end_y=sta_y+1
        elif di is 'D':
            end_y=sta_y-1
        
        #만일 abs(end_x)>5 or abs(end_y)>5 라면?
        if abs(end_x)>5:
            end_x=(lambda x:5 if x>0 else -5)(end_x)
        if abs(end_y)>5:
            end_y=(lambda y:5 if y>0 else -5)(end_y)     
        
        #print([sta_x, sta_y, end_x, end_y] )
        # sta_x와 end_x는 서로 달라야한다.
        if (sta_x != end_x) or (sta_y!=end_y):
            # arrows에 존재하지 않는다면 추가.
            if([sta_x, sta_y, end_x, end_y] in arrows)is False:
                arrows.append([sta_x, sta_y, end_x, end_y])
                #반대방향도 포함된다.
                arrows.append([end_x, end_y, sta_x, sta_y])
            # arrows 존재여부 상관없이 sta_x, sta_y는 갱신된다.
            sta_x= end_x
            sta_y=end_y   
    return len(arrows)/2
