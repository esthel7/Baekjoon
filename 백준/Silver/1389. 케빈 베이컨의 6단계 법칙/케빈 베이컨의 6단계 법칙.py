import sys
from collections import deque
input=sys.stdin.readline

N,M=map(int,input().split())
graph={}
for i in range(M):
  A,B=map(int,input().split())
  if A in graph:
    graph[A][B]=True
  else:
    graph[A]={B:True}
  if B in graph:
    graph[B][A]=True
  else:
    graph[B]={A:True}

answer=[-1,-1]
for i in range(1,N+1):
  l=[-1 for i in range(N+1)]
  l[i]=0
  q=deque([i])
  while q:
    node=q.popleft()
    if node not in graph:
      continue
    for item in graph[node]:
      if l[item]==-1:
        l[item]=l[node]+1
        q.append(item)
  total=sum(l)
  if answer[0]==-1 or answer[0]>total:
    answer=[total,i]

print(answer[1])
