import sys
from collections import deque
input=sys.stdin.readline

T=int(input())
for _ in range(T):
  def find():
    q=deque(root.keys())
    visited=[-1 for i in range(N+1)]
    while q:
      node=q.popleft()
      if visited[node]==-1:
        visited[node]=time[node]
      if node in outs:
        for nextnode in outs[node]:
          visited[nextnode]=max(visited[nextnode],time[nextnode]+visited[node])
          if node in ins[nextnode]:
            ins[nextnode].pop(node)
            if not ins[nextnode]:
              q.append(nextnode)

    print(visited[target])



  N,K=map(int,input().split())
  time=[0]+list(map(int,input().split()))
  root={}
  for i in range(1,N+1):
    root[i]=True
  ins={}
  outs={}
  for i in range(K):
    start,end=map(int,input().split())
    if end in ins:
      ins[end][start]=True
    else:
      ins[end]={start:True}
    if start in outs:
      outs[start][end]=True
    else:
      outs[start]={end:True}
    if end in root:
      root.pop(end)

  target=int(input())
  find()
