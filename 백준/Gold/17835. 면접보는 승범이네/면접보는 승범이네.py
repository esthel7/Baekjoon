import sys
import heapq
from collections import deque
input=sys.stdin.readline

N,M,K=map(int,input().split())
graph={}
for i in range(M):
  u,v,c=map(int,input().split())
  if v in graph:
    if u in graph[v]:
      graph[v][u]=min(graph[v][u],c)
    else:
      graph[v][u]=c
  else:
    graph[v]={u:c}

l=list(map(int,input().split()))

last=10000000000
dis=deque([last for i in range(N+1)])
q=[]
for place in l:
  dis[place]=0
  heapq.heappush(q,[0,place])

while q:
  cost,place=heapq.heappop(q)
  if place not in graph or dis[place]!=cost:
    continue
  for node in graph[place]:
    if dis[node]>cost+graph[place][node]:
      dis[node]=cost+graph[place][node]
      heapq.heappush(q,[cost+graph[place][node],node])

dis.popleft()
Max=max(dis)
print(dis.index(Max)+1)
print(Max)
