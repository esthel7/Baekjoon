import sys
input=sys.stdin.readline

def find(lL):
    s.append(l[0])
    for i in range(1,lL):
        flag=0
        I=len(l[i])
        for j in range(len(s)):
            if s[j][:I]==l[i]:
                flag=1
                break
        if flag==0:
            s.append(l[i])
    print(len(s))

N=int(input())
l=[]
for i in range(N):
    l.append(input().rstrip())

l=list(set(l)) # 중복제거
lL=len(l)
for i in range(lL):
    l[i]=list(l[i])
l=sorted(l,key=len,reverse=True) # 가장 긴 단어부터 오도록
s=[]
find(lL)
