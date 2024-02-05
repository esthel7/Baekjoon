import sys
import heapq
input=sys.stdin.readline

N=int(input())
l=[]
for i in range(N):
  l.append(list(map(int,input().split())))
l.sort()

cnt=[0]
heapq.heapify(cnt)
for i in range(N):
  start=l[i][0]
  end=l[i][1]
  now=heapq.heappop(cnt)
  if now<=start:
    heapq.heappush(cnt,end)
  else:
    heapq.heappush(cnt,now)
    heapq.heappush(cnt,end)
print(len(cnt))
