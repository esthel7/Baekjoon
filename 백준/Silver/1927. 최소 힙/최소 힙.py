import sys
import heapq
input=sys.stdin.readline

N=int(input())
l=[]
heapq.heapify(l)

for i in range(N):
  x=int(input())
  if x>0:
    heapq.heappush(l,x)
  else:
    if not l:
      print(0)
    else:
      print(heapq.heappop(l))
  
