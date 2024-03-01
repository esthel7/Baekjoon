import sys
from collections import deque
input=sys.stdin.readline

N,M=map(int,input().split())
degree=[0 for i in range(N+1)]
back=[[]for i in range(N+1)]
for i in range(M):
  f,s=map(int,input().split())
  back[f].append(s)
  degree[s]+=1

q=deque([])
for i in range(1,N+1):
  if degree[i]==0:
    q.append(i)

answer=[]
while q:
  now=q.popleft()
  answer.append(now)
  for node in back[now]:
    degree[node]-=1
    if degree[node]==0:
      q.append(node)

for item in answer:
  print(item,end=' ')
