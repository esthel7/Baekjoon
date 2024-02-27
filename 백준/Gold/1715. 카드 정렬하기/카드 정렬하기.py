import sys
import heapq
input=sys.stdin.readline

N=int(input())
l=[]
for i in range(N):
  l.append(int(input()))

if N==1:
  print(0)
  exit(0)

heapq.heapify(l)
answer=0
while len(l)>=2:
  first=heapq.heappop(l)
  second=heapq.heappop(l)
  answer+=first+second
  heapq.heappush(l,first+second)

print(answer)
