import sys
input=sys.stdin.readline

l=list(input().rstrip())

flag=0
common=[]
q=[] # 변수형
word=[] # 변수
for i in range(len(l)):
    if l[i]==' ':
        if flag==0:
            word=[]
            q=[]
            flag=1
            common=l[:i] # 공통 변수형
        continue
    if l[i]==',' or l[i]==';':
        for i in range(len(common)):
            print(common[i],end='')
        for i in range(len(q)):
            print(q[len(q)-i-1],end='')
        print(' ',end='')
        for i in range(len(word)):
            print(word[i],end='')
        print(';')
        word=[]
        q=[]
        continue
    if l[i]=='[':
        q.append(']')
        q.append('[')
    elif l[i]==']':
        continue
    elif l[i]=='*' or l[i]=='&':
        q.append(l[i])
    else:
        word.append(l[i])
