import sys
import heapq
input=sys.stdin.readline

def find():
  global answer
  q=[]
  Max=-1
  for i in range(N):
    heapq.heappush(q,[l[i][0],i,0])
    Max=max(Max,l[i][0])
  answer=Max-q[0][0]

  while True:
    num,x,y=heapq.heappop(q)
    if y!=M-1:
      heapq.heappush(q,[l[x][y+1],x,y+1])
      Max=max(Max,l[x][y+1])
      answer=min(answer,Max-q[0][0])
    else:
      break



N,M=map(int,input().split())
l=[]
for i in range(N):
  now=list(map(int,input().split()))
  now.sort()
  l.append(now)

answer=0
find()

print(answer)
