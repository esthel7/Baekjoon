import sys
import heapq
input=sys.stdin.readline

N=int(input())
M=int(input())

q=[]
for i in range(M):
  a,b,c=map(int,input().split())
  if a==b:
    continue
  heapq.heappush(q,[c,a,b])

answer=0
root=[0 for i in range(N+1)]
while q:
  [c,a,b]=heapq.heappop(q)
  if root[a]==0:
    if root[b]==0:
      root[a]=a
      root[b]=a
      answer+=c
    else:
      root[a]=root[b]
      answer+=c
  else:
    if root[b]==0:
      root[b]=root[a]
      answer+=c
    else:
      if root[a]!=root[b]:
        change=root[b]
        for i in range(N+1):
          if root[i]==change:
            root[i]=root[a]
        answer+=c

print(answer)
