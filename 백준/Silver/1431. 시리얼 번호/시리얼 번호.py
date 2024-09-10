import sys
import heapq
input=sys.stdin.readline

N=int(input())
q=[]
for i in range(N):
  now=list(input().rstrip())
  Now=len(now)
  cnt=0
  for j in range(Now):
    if '0'<=now[j]<='9':
      cnt+=int(now[j])
  heapq.heappush(q,[Now,cnt,now])

while q:
  Now,cnt,now=heapq.heappop(q)
  print(''.join(now))
