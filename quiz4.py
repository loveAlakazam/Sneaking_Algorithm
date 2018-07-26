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
#correct answer
def solution(n):
    #채워넣기
    nums=[]
    for i in range(0,n+1): #0~n
        nums.append(i)
    
    for i in range(2,n+1):#2~n
        if nums[i]==0:
            continue
        j=i*2
        while(j<=n):
            nums[j]=0
            j+=i

    answer = 0
    for i in range(2,n+1):
        if nums[i]!=0:
            answer+=1
    return answer
