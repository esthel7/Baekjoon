import sys
import heapq
input=sys.stdin.readline

N,M=map(int,input().split())

graph={}
for i in range(M):
  A,B,C=map(int,input().split())
  if A==B:
    continue
  if A not in graph:
    graph[A]={}
  if B not in graph:
    graph[B]={}

  if B in graph[A] and graph[A][B]>C:
    continue
  graph[A][B]=C
  graph[B][A]=C

S,E=map(int,input().split())

visit={}
q=[]
for node in graph[S]:
  visit[node]=graph[S][node]
  heapq.heappush(q,[-graph[S][node],node])

while q:
  cost,node=heapq.heappop(q)
  cost*=(-1)
  if node==E:
    print(cost)
    break

  for nextNode in graph[node]:
    if nextNode==S:
      continue
    nowCost=graph[node][nextNode]
    Min=min(cost,nowCost)
    if nextNode in visit and visit[nextNode]>=Min:
      continue
    visit[nextNode]=Min
    heapq.heappush(q,[-Min,nextNode])
