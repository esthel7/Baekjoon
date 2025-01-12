import sys
import heapq
input=sys.stdin.readline

N=int(input())
l=[]
for i in range(N):
  x,y=map(float,input().split())
  l.append([x,y])

q=[]
# diff=[[0 for i in range(N)]for j in range(N)]
for i in range(N):
  a,b=l[i]
  for j in range(i+1,N):
    c,d=l[j]
    cal=((a-c)**2+(b-d)**2)**0.5
    heapq.heappush(q,[cal,i,j])
    # diff[i][j]=cal
    # diff[j][i]=cal

answer=0
root=[-1 for i in range(N)]
while q:
  now,a,b=heapq.heappop(q)
  if root[a]==-1:
    if root[b]==-1:
      root[a]=a
      root[b]=a
      answer+=now
    else:
      root[a]=root[b]
      answer+=now
  else:
    if root[b]==-1:
      root[b]=root[a]
      answer+=now
    else:
      if root[a]==root[b]:
        continue
      Min=min(root[a],root[b])
      Max=max(root[a],root[b])
      for i in range(N):
        if root[i]==Min:
          root[i]=Max
      answer+=now

print('%.2lf'%answer)
