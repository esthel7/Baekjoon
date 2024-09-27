import sys
import heapq
input=sys.stdin.readline

N=int(input())
loc=[]
for i in range(N):
  a,b=map(int,input().split())
  loc.append([a,b]) # 거리, 주유
loc.sort()

L,P=map(int,input().split())
current=P
cnt=0

q=[]
last=0
while True:
  if current>=L:
    print(cnt)
    break

  for i in range(last,N):
    if loc[i][0]<=current:
      heapq.heappush(q,[-loc[i][1],loc[i][0]])
      if i==N-1:
        last=N
    else:
      last=i
      break

  if not q:
    print(-1)
    break

  go,now=heapq.heappop(q)
  current+=-go
  cnt+=1
