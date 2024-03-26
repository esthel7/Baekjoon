import sys
import heapq
input=sys.stdin.readline

N=int(input())
l=[]
heapq.heapify(l)
for i in range(N):
  now=list(map(int,input().split()))
  now.sort(reverse=True)
  for j in range(N):
    if len(l)<N:
      heapq.heappush(l,now[j])
      continue
    if l[0]<now[j]:
      heapq.heappop(l)
      heapq.heappush(l,now[j])
    else:
      break

print(l[0])
