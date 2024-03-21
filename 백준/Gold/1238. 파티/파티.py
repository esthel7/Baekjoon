import sys
import heapq
input=sys.stdin.readline

N,M,X=map(int,input().split())
graph=[[]for i in range(N+1)]
grp=[[]for i in range(N+1)]
for i in range(M):
  a,b,c=map(int,input().split())
  graph[b].append([c,a]) # cost, 출발 node
  grp[a].append([c,b]) # cost, 도착 node

go=[0 for i in range(N+1)]
go[X]=1
q=[]
heapq.heapify(q)
for [c,nextnode] in graph[X]:
  heapq.heappush(q,[c,nextnode])
while q:
  cnt,node=heapq.heappop(q)
  if go[node]==0 or go[node]>cnt:
    go[node]=cnt
    for [c,nextnode] in graph[node]:
      heapq.heappush(q,[c+cnt,nextnode])

arrive=[0 for i in range(N+1)]
arrive[X]=1
q=[]
heapq.heapify(q)
for [c,nextnode] in grp[X]:
  heapq.heappush(q,[c,nextnode])
while q:
  cnt,node=heapq.heappop(q)
  if arrive[node]==0 or arrive[node]>cnt:
    arrive[node]=cnt
    for [c,nextnode] in grp[node]:
      heapq.heappush(q,[c+cnt,nextnode])

Max=go[1]+arrive[1]
for i in range(2,N+1):
  now=go[i]+arrive[i]
  if now>Max:
    Max=now

print(Max)
