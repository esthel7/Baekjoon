import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
m=int(input())

graph={}
for i in range(1,n+1):
  graph[i]={}

for i in range(m):
  start,end,cost=map(int,input().split())
  if end in graph[start]:
    if graph[start][end]>cost:
      graph[start][end]=cost
  else:
    graph[start][end]=cost

start,end=map(int,input().split())

l=[-1 for i in range(n+1)]
l[start]=0
cnt=[[] for i in range(n+1)]
visited=[False for i in range(n+1)]

q=deque([start])
while q:
  now=q.popleft()
  visited[now]=False
  for node in graph[now]:
    if (l[node]==-1 or l[node]>graph[now][node]+l[now]) and (l[end]==-1 or l[end]>graph[now][node]+l[now]):
      l[node]=graph[now][node]+l[now]
      cnt[node]=list(cnt[now])
      cnt[node].append(now)
      if not visited[node] and node!=end:
        q.append(node)
        visited[node]=True

print(l[end])
cnt[end].append(end)
print(len(cnt[end]))
for answer in cnt[end]:
  print(answer,end=' ')
print()
