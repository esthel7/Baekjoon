import sys
from collections import deque
input=sys.stdin.readline

parent={}
child={}
n=int(input())
for i in range(1,n+1):
  parent[i]=0
  child[i]=[]

a,b=map(int,input().split())
m=int(input())
for i in range(m):
  x,y=map(int,input().split())
  child[x].append(y)
  parent[y]=x

visit=[False for i in range(n+1)]
visit[b]=True
q=deque([[b,0]])
while q:
  item,rel=q.popleft()
  if item==a:
    print(rel)
    exit(0)
  if parent[item]!=0 :
    if not visit[parent[item]]:
      visit[parent[item]]=True
      q.append([parent[item],rel+1])
    for nextItem in child[parent[item]]:
      if not visit[nextItem]:
        visit[nextItem]=True
        q.append([nextItem,rel+2])
  for nextItem in child[item]:
    if not visit[nextItem]:
      visit[nextItem]=True
      q.append([nextItem,rel+1])

print(-1)
