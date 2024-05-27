import sys
import heapq
input=sys.stdin.readline

V,E=map(int,input().split())
graph={}

K=int(input())
l=[]
for i in range(E):
  u,v,w=map(int,input().split())
  if u in graph:
    if v in graph[u]:
      if graph[u][v]>w:
        graph[u][v]=w
    else:
      graph[u][v]=w
  else:
    graph[u]={v:w}


q=[]
if K in graph:
  for node in graph[K]:
    if graph[K][node]!=0 and graph[K][node]!=-1:
      heapq.heappush(q,[graph[K][node],node])

answer=[-1 for i in range(V+1)]
answer[K]=0
while q:
  cost,node=heapq.heappop(q)
  if answer[node]==-1 or answer[node]>cost:
    answer[node]=cost
    if node in graph:
      for nextNode in graph[node]:
        heapq.heappush(q,[graph[node][nextNode]+cost,nextNode])

for i in range(1,V+1):
  if i==K:
    print(0)
  elif answer[i]==-1:
    print('INF')
  else:
    print(answer[i])
