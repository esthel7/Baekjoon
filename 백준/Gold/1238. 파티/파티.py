import sys
import heapq
input=sys.stdin.readline

N,M,X=map(int,input().split())

graph={}
rgraph={}
for i in range(1,N+1):
  graph[i]={i:0}
  rgraph[i]={i:0}

for i in range(M):
  start,end,time=map(int,input().split())
  graph[start][end]=time
  rgraph[end][start]=time

go=[-1 for i in range(N+1)]
go[X]=0
q=[]
for key in rgraph[X].keys():
  go[key]=rgraph[X][key]
  heapq.heappush(q,[rgraph[X][key],key])
while q:
  cost,node=heapq.heappop(q)
  for key in rgraph[node].keys():
    if go[key]==-1 or go[key]>cost+rgraph[node][key]:
      go[key]=cost+rgraph[node][key]
      heapq.heappush(q,[go[key],key])

arrive=[-1 for i in range(N+1)]
arrive[X]=0
q=[]
for key in graph[X].keys():
  arrive[key]=graph[X][key]
  heapq.heappush(q,[graph[X][key],key])
while q:
  cost,node=heapq.heappop(q)
  for key in graph[node].keys():
    if arrive[key]==-1 or arrive[key]>cost+graph[node][key]:
      arrive[key]=cost+graph[node][key]
      heapq.heappush(q,[arrive[key],key])

answer=0
for i in range(1,N+1):
  answer=max(answer,go[i]+arrive[i])

print(answer)
