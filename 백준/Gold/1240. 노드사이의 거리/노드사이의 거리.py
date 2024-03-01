import sys
from collections import deque
input=sys.stdin.readline

def find(a,b,N):
  visited=[False for i in range(N+1)]
  q=deque([])
  visited[a]=True
  for [node,far] in tree[a]:
    if node==b:
      print(far)
      return
    q.append([node,far])
    visited[node]=True

  while q:
    a,nextFar=q.popleft()
    for [node,far] in tree[a]:
      if node==b:
        print(nextFar+far)
        return
      if not visited[node]:
        visited[node]=True
        q.append([node,nextFar+far])



N,M=map(int,input().split())
tree=[[]for i in range(N+1)]

for i in range(N-1):
  a,b,f=map(int,input().split())
  tree[a].append([b,f]) # 점, 거리
  tree[b].append([a,f])

for i in range(M):
  a,b=map(int,input().split())
  find(a,b,N)
