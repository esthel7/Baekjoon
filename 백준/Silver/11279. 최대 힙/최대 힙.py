import sys
import heapq
input=sys.stdin.readline

N=int(input())
l=[]
for i in range(N):
  x=int(input())
  if x==0:
    if not len(l):
      print(0)
    else:
      print((-1)*heapq.heappop(l))
  else:
    heapq.heappush(l,-x)
