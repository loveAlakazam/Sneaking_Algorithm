# 현재 테스트케이스 통과 상태: 아직 통과되지 못함.
# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/42840?language=python3
def reIndex( i, len_g): #i는 현재 인덱스 위치, len_g= (len_g1/len_g2/len_g3)의 길이
    if i<len_g:
        return i
    else: #i>=len_g
        return reIndex(i-len_g, len_g)
    
def solution(answers):
    g1=[1,2,3,4,5]
    g2=[2,1,2,3,2,4,2,5]
    g3=[3,3,1,1,2,2,4,4,5,5]
    len_g1=len(g1) #5
    len_g2=len(g2) #8
    len_g3=len(g3) #10
    len_a= len(answers)
    cnt=[0,0,0]
    for i in range(len_a):
        #len_g1=5
        if i>=len_g1:
            idx= reIndex(i, len_g1)
        else:#i<len_g1
            idx=i
        if answers[i]==g1[idx]:
            cnt[0]+=1
            
        #len_g2=8
        if i>=len_g2:
            idx= reIndex(i, len_g2)
        else:#i<len_g1
            idx=i
        if answers[i]==g2[idx]:
            cnt[1]+=1
        
        #len_g3=10
        if i>=len_g3:
            idx= reIndex(i, len_g3)
        else:#i<len_g1
            idx=i
        if answers[i]==g3[idx]:
            cnt[2]+=1
    
    max_cnt= max(cnt)
    result=[]
    for i in range(3):
        if cnt[i]==max_cnt:
            result.append(i+1)
    return result
    
        
    
            
   
            
        
        
    
