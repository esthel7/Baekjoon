import sys
input=sys.stdin.readline

N=int(input())
l=[]
for i in range(N):
    l.append(input().rstrip())
l=list(set(l))
l.sort(key=len)
N=len(l)
# print(l)

# 한 단어라도 어느 단어 앞에 포함되면 안됨
count=0
for i in range(N):
    I=len(l[i])
    flag=0
    for j in range(i+1,N):
        if l[j][:I] == l[i]:
            flag=1
            break
    if flag==0:
        count+=1
print(count)
