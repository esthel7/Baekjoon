import sys
from collections import deque
input=sys.stdin.readline

T=int(input())
for _ in range(T):
  N,M=map(int,input().split())
  graph={}
  for i in range(1,N+1):
    graph[i]={}
  for i in range(M):
    a,b=map(int,input().split())
    graph[a][b]=True
    graph[b][a]=True
  visited=[False for i in range(N+1)]
  visited[1]=True
  q=deque([1])
  answer=-1
  while q:
    node=q.popleft()
    answer+=1
    for nextNode in graph[node]:
      if not visited[nextNode]:
        visited[nextNode]=True
        q.append(nextNode)
  print(answer)

