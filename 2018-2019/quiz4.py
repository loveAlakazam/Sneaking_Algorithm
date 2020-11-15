#view question: https://programmers.co.kr/learn/courses/30/lessons/12921?language=python3
#reference: http://marobiana.tistory.com/91 
#wrong answer(time out)
'''
#이렇게 풀면 안됨 
def isPrime(x):
    count =1
    for i in range(2,x+1):#2~x중에서 x와 나누어떨어지는 수를 찾는다.
        if x%i==0:
            count+=1
    return count

def solution(n):
    prime =[]
    for i in range(2,n+1):#2~n중에서 소수를 찾는다.(1은 소수가 아니다.)
        if i==2 or i%2 !=0: #2가 아닌 짝수는 소수가 될 수 없다
            if isPrime(i)==2:
                prime.append(i)

    answer = len(prime)
    return answer

'''
#correct answer (에라토스테네스 체 이용하기 => 검색해서 알게됨...)
def solution(n):
    #채워넣기
    nums=[]
    for i in range(0,n+1): #0~n
        nums.append(i)
    
    for i in range(2,n+1):#나누는 값 2~n (인덱스번호와 값은 동일: nums[2]=2)
        if nums[i]==0: #이미 체크된 배수는 확인하지 않는다.
            continue
        #i를 제외한 i의 배수들은 모두 0으로 한다.    
        j=i*2
        while(j<=n): 
            nums[j]=0
            j+=i

    answer = 0
    for i in range(2,n+1):
        if nums[i]!=0:
            answer+=1
    return answer
