# -*- encoding:utf-8 -*-
def isAlphabet(strings): 
    alphabetCount=0
    for i in strings:
        if i.isalpha()==True:
            alphabetCount+=1
    if alphabetCount==len(strings):
        return True
    else:
        return False

def shortestElement(strings):
    index=0 #index=0으로 초기화
    for i in range (len(strings)): #0~len(strings)-1까지
        if len(strings[i])<len(strings[index]):
            index=i
    return index #가장길이가 짧은원소의 index번호

def solution(strings,n):
    alphabet={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
    #string의 모든 원소들은 알파벳으로 구성되어있는가?
    if isAlphabet(strings)==True:
        #strings를 오름차순으로 정렬
        strings.sort()
        
        #모든 strings의 원소들을 소문자로 한다.
        for i in range(len(strings)):
            strings[i]=strings[i].lower()

        #strings에서 가장짧은원소의 길이(shortest) >n인가?
        shortest=len(strings[shortestElement(strings)])
        if shortest>n:
            j=0
            while(j<len(strings)):
                for i in range(len(strings)-1): #버블정렬로 나열...^^;
                    if alphabet[strings[i][n]]>alphabet[strings[i+1][n]]:
                        tmp=strings[i]
                        strings[i]=strings[i+1]
                        strings[i+1]=tmp
                j+=1

        return strings
