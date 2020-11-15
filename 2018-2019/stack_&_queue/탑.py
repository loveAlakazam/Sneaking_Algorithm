def solution(heights):
    len_h= len(heights)
    answer = []
    heights.reverse()
    for i in range(len_h-1):#i=0~len_h-2 
        check=0
        for j in range(i+1,len_h):#j=i+1,...,len_h-1
            if check==0 and heights[i]<heights[j]:
                check=1
                answer.append(len_h-j)
        if check==0:
            answer.append(0)
    answer.append(0)
    answer.reverse()
    return answer
