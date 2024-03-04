import sys
import heapq
input=sys.stdin.readline

n,m,r=map(int,input().split())
item=[0]+list(map(int,input().split()))

graph=[[]for i in range(n+1)]
for _ in range(r):
  a,b,L=map(int,input().split())
  if L>m:
    continue
  graph[a].append([b,L]) # node, len
  graph[b].append([a,L])

answer=0
for i in range(1,n+1):
  visited=[-1 for i in range(n+1)]
  q=[[0,i]]
  heapq.heapify(q)
  visited[i]=0

  while q:
    [now,idx]=heapq.heappop(q)
    for [node,L] in graph[idx]:
      if visited[node]==-1:
        visited[node]=now+L
      elif visited[node]>now+L:
        visited[node]=now+L
      else:
        continue

      heapq.heappush(q,[now+L,node])

  cnt=0
  for j in range(1,n+1):
    if visited[j]<=m and visited[j]!=-1:
      cnt+=item[j]

  if answer<cnt:
    answer=cnt

print(answer)
