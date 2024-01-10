import sys
from collections import deque
input=sys.stdin.readline

def find(m,n,M,N):
  mbox=[-1,1,0,0]
  nbox=[0,0,-1,1]
  cnt=0
  q=deque([[m,n]])
  while q:
    [m,n]=q.popleft()
    if 0<=m<M and 0<=n<N and l[m][n]==0:
      l[m][n]=1
      cnt+=1
      for i in range(4):
        q.append([m+mbox[i],n+nbox[i]])
  return cnt


M,N,K=map(int,input().split())
l=[[0 for i in range(N)]for j in range(M)]
for i in range(K):
  rect=list(map(int,input().split()))
  # M-rect[1]-1 rect[0] (왼쪽아래) M-rect[3] rect[2]-1 (오른쪽위)
  for a in range(M-rect[3],M-rect[1]):
    for b in range(rect[0],rect[2]):
      l[a][b]=1

cnt=0
boxes=[]
for i in range(M):
  for j in range(N):
    if l[i][j]==0:
      boxes.append(find(i,j,M,N))
      cnt+=1

print(cnt)
boxes.sort()
for box in boxes:
  print(box,end=' ')
