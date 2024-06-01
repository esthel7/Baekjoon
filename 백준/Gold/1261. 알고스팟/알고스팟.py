import sys
import heapq
input=sys.stdin.readline

# 빈 방에 이동 가능

y,x=map(int,input().split())
l=[]
for i in range(x):
  l.append(list(input().rstrip()))

xbox=[-1,1,0,0]
ybox=[0,0,-1,1]

visit=[[-1 for i in range(y)]for j in range(x)]
q=[[0,0,0]]
while q:
  cnt,i,j=heapq.heappop(q)
  if visit[i][j]==-1 or visit[i][j]>cnt:
    visit[i][j]=cnt
    for k in range(4):
      newI=i+xbox[k]
      newJ=j+ybox[k]
      if 0<=newI<x and 0<=newJ<y:
        if l[newI][newJ]=='0':
          heapq.heappush(q,[cnt,newI,newJ])
        else:
          heapq.heappush(q,[cnt+1,newI,newJ])

print(visit[x-1][y-1])
