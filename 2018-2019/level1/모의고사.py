# 문제 링크
# https://programmers.co.kr/learn/courses/30/lessons/42840?language=python3
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
        if g1[i%len_g1]==answers[i]:
            cnt[0]+=1
        if g2[i%len_g2]==answers[i]:
            cnt[1]+=1
        if g3[i%len_g3]==answers[i]:
            cnt[2]+=1

    max_cnt= max(cnt)
    result=[]
    for i in range(3):
        if cnt[i]==max_cnt:
            result.append(i+1)
    return result
