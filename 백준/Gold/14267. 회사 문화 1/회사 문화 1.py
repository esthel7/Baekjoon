import sys
from collections import deque
input=sys.stdin.readline

n,m=map(int,input().split())
parent=[-1]+list(map(int,input().split())) # 직속상사 담기

children=[[]for i in range(n+1)] # 직속부하 담기
for i in range(2,n+1):
  parentidx=parent[i]
  children[parentidx].append(i)

final=[0 for i in range(n+1)]
for i in range(m):
  idx,w=map(int,input().split())
  final[idx]+=w

q=deque([1])
while q:
  now=q.popleft()
  cnt=final[now]
  for node in children[now]:
    final[node]+=cnt
    q.append(node)

for i in range(1,n+1):
  print(final[i],end=' ')

