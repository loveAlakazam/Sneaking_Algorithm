class Solution:
    def findKthPositive(self, k: int, arr) -> int:
        n=0 #arr에 포함되지 않은 숫자 인덱스
        i=1 #현재 숫자
        while (True):
            # i 가 arr에 들어있지 않는다면, n이 카운트된다.
            if i not in arr:
                n+=1
            
            if n==k:
                return i
            i+=1