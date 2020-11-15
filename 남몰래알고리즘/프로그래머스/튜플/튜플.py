def solution(s):
    answer = []
    tmp=[  [int(e) for e in x.split(',')] for x in s[2:-2].split('},{')]
    tmp=sorted(tmp, key=len)
    
    for t in tmp:
        for e in t:
            if e not in answer:
                answer.append(e)
    return answer
