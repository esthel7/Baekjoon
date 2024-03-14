import sys
from collections import deque
input=sys.stdin.readline

N,M=map(int,input().split())
graph=[[]for i in range(N+1)]
for i in range(M):
  a,b,c=map(int,input().split())
  graph[a].append([b,c]) # node, cost
  graph[b].append([a,c])

q=deque([[1,0]])
cost=[-1 for i in range(N+1)]
cost[1]=0
answer=-1
while q:
  node,cnt=q.popleft()
  if cost[node]!=cnt:
    continue
  if node==N:
    if answer==-1 or answer>cnt:
      answer=cnt
    continue
  for [nextnode,c] in graph[node]:
    now=cnt+c
    if cost[nextnode]==-1 or cost[nextnode]>now:
      cost[nextnode]=now
      q.append([nextnode,now])

print(answer)
