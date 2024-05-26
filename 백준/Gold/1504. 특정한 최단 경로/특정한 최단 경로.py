import sys
import heapq
input=sys.stdin.readline

def find(start):
  visit=[Last for i in range(N+1)]
  q=[]
  heapq.heappush(q,[0,start])
  while q:
    cost,node=heapq.heappop(q)
    if visit[node]>cost:
      visit[node]=cost
      if node not in graph:
        continue
      for nextNode in graph[node]:
        heapq.heappush(q,[graph[node][nextNode]+cost,nextNode])

  if start not in graph:
    graph[start]={}
  for i in range(1,N+1):
    if i in graph[start]:
      if graph[start][i]>visit[i]:
        graph[start][i]=visit[i]
    else:
      graph[start][i]=visit[i]


N,E=map(int,input().split())
Last=2000*(N+1)

graph={}
for i in range(E):
  start,end,cost=map(int,input().split())
  if start in graph:
    if end in graph[start]:
      if graph[start][end]>cost:
        graph[start][end]=cost
    else:
      graph[start][end]=cost
  else:
    graph[start]={end:cost}

  if end in graph:
    if start in graph[end]:
      if graph[end][start]>cost:
        graph[end][start]=cost
    else:
      graph[end][start]=cost
  else:
    graph[end]={start:cost}

u,v=map(int,input().split())

find(1)
find(u)
find(v)

value=min(graph[1][u]+graph[u][v]+graph[v][N],graph[1][v]+graph[v][u]+graph[u][N])
if value<Last:
  print(value)
else:
  print(-1)

