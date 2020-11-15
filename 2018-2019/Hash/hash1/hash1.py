# https://programmers.co.kr/learn/courses/30/lessons/42576?language=python3
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i]!=completion[i]:
            return participant[i]
    return participant[i+1]
    
    '''
    #시간복잡도 O(N^2)인 경우의 코드..
    #list.remove()와 반복문을 동시에 사용하면 시간복잡도가 O(N)이됨.
    def solution(participant, completion):
      for c in completion:
      participant.remove(c)
      return participant[0]
    
    '''
