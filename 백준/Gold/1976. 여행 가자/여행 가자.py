import sys
from collections import deque
input=sys.stdin.readline

N=int(input())
M=int(input())

graph={}
for i in range(N):
  graph[i]=[]

for i in range(N):
  now=list(map(int,input().split()))
  for j in range(i,N):
    if now[j]==1:
      graph[i].append(j)
      graph[j].append(i)

plan=list(map(int,input().split()))
plan=list(set(plan))
M=len(plan)
for i in range(M):
  plan[i]-=1

if M==1:
  print('YES')
  # if plan[0] in graph[plan[0]]:
  #   print('YES')
  # else:
  #   print('NO')
  exit(0)

visited=[False for i in range(N)]
q=deque([])
goal=1
visited[plan[0]]=True
for item in graph[plan[0]]:
  visited[item]=True
  q.append([item,goal])

while q:
  node,target=q.popleft()
  if node==plan[target]:
    goal+=1
    if goal==M:
      print('YES')
      exit(0)
    visited=[False for i in range(N)]
    visited[node]=True
    q=deque([])

  for item in graph[node]:
    if visited[item]:
      continue
    visited[item]=True
    q.append([item,goal])

print('NO')
