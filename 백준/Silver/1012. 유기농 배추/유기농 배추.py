import sys
input=sys.stdin.readline

def change(l,x,y,M,N):
  q=[[x,y]]
  while q:
    [x,y]=q.pop()
    if x>=N or y>=M or x<0 or y<0:
      continue
    if l[x][y]==1:
      l[x][y]=0
      q.append([x-1,y])
      q.append([x+1,y])
      q.append([x,y-1])
      q.append([x,y+1])
  return l


T=int(input())
for i in range(T):
  M,N,K=map(int,input().split())
  l=[[0 for a in range(M)] for b in range(N)]
  for j in range(K):
    x,y=map(int,input().split())
    l[y][x]=1
  
  cnt=0
  for i in range(N):
    for j in range(M):
      if l[i][j]==1:
        l=change(l,i,j,M,N)
        cnt+=1
  print(cnt)
