import sys
from collections import deque
input=sys.stdin.readline

N,M=map(int,input().split())
degree=[0 for i in range(N+1)]
back=[[]for i in range(N+1)] # 뒤 요소들 보관

for i in range(M):
  l=deque(map(int,input().split()))
  t=l.popleft()
  for j in range(1,t):
    degree[l[j]]+=1
    back[l[j-1]].append(l[j])

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

if len(answer)==N:
  for item in answer:
    print(item)
else:
  print(0)
