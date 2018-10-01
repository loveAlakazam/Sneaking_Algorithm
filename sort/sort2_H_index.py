# https://programmers.co.kr/learn/courses/30/lessons/42747?language=python3
def solution(citations):
    citations.sort(reverse=True)
    if len(citations)<1:
        return 0    
    for c in range(len(citations)):
        if c >= citations[c]:
            return c
    return c+1

'''
citations=[3,0,6,1,5] ==> sort==> [6,5,3,1,0]
index= 0 ~ len(citations)

(ex1)
citations       index
 6      >       0
 5      >       1
 3      >       2
 -------------------return 3
 1      <       3
 0      <       4
 
 (ex2)
 citations      index
 5      >       0
 4      >       1
 --------------------return 2
 2      =       2
 1      <       3
 
 (ex3)
 citations      index
 122    >       0
 71     >       1
 51     >       2
 22     >       3
 --------------------return 4
 2      <       4
'''
