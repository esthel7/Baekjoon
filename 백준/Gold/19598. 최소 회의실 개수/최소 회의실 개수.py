import sys
import heapq
input=sys.stdin.readline

N=int(input())
l=[]
for i in range(N):
  l.append(list(map(int,input().split())))
l.sort()

answer=0
room=[]
heapq.heapify(room)
for i in range(N):
  while room:
    if room[0]<=l[i][0]:
      heapq.heappop(room)
    else:
      break
  heapq.heappush(room,l[i][1])
  Len=len(room)
  if Len>answer:
    answer=Len

print(answer)
