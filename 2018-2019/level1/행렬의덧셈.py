# https://programmers.co.kr/learn/courses/30/lessons/12950?language=python3
def solution(arr1, arr2):
    arr3=[]
    row=len(arr1)     #행
    col=len(arr1[0])  #열
    for r in range(row):
        arr3.append([])
        for c in range(col):
            arr3[r].append(arr1[r][c]+arr2[r][c])
    return arr3
