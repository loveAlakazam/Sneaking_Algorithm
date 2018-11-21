def solution(s):
    a = list(s)
    r=-1
    for i in range(len(a)):
        if a[i]==' ':
            r=i
        if (a[i].isalpha()==True):
            if (i-r)%2==0:
                a[i]=a[i].lower()
            else: #(i-r)%2!=0
                a[i]=a[i].upper()
    return ''.join(a)
