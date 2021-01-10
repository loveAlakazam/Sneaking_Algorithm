import sys
input=sys.stdin.readline
usedAlpha=['-1']*26
S=input()

for idx,s in enumerate(list(S[:-1])):
    now=ord(s)-ord('a')
    if usedAlpha[now]=='-1':
        usedAlpha[now]=str(idx)

print(' '.join(usedAlpha))

