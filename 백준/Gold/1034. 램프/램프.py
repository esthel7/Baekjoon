import sys
input=sys.stdin.readline

N,M=map(int,input().split())
l=[]
for i in range(N):
  l.append(list(input().rstrip()))
K=int(input())

answer=0
for i in range(N):
  change={}
  for j in range(M):
    if l[i][j]=='0':
      change[j]=True
  Len=len(change.keys())
  if Len<=K and Len%2==K%2:
    now=1
    for j in range(i+1,N):
      flag=True
      for k in range(M):
        if k in change:
          if l[j][k]=='1':
            flag=False
            break
        else:
          if l[j][k]=='0':
            flag=False
            break
      if flag:
        now+=1
    answer=max(answer,now)

print(answer)
