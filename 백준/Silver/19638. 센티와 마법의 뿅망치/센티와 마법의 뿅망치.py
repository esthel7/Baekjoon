import sys
import heapq
input=sys.stdin.readline

N,H,T=map(int,input().split())
q=[]
for i in range(N):
  h=int(input())
  heapq.heappush(q,-h)

cnt=0
for i in range(T):
  if q[0]*(-1)<H:
    break
  cnt+=1
  now=heapq.heappop(q)
  now*=(-1)
  if now!=1:
    heapq.heappush(q,now//2*(-1))
  else:
    heapq.heappush(q,-1)

if q[0]*(-1)<H:
  print('YES')
  print(cnt)
else:
  print('NO')
  print(-q[0])
