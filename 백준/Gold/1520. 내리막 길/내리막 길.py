import sys
input=sys.stdin.readline

M,N=map(int,input().split())
l=[]
for i in range(M):
  l.append(list(map(int,input().split())))

xbox=[-1,1,0,0]
ybox=[0,0,-1,1]
visited=[[False for i in range(N)]for j in range(M)]
cnt=[[0 for i in range(N)]for j in range(M)]
cnt[0][0]=1

def update(x,y,plus):
  cnt[x][y]+=plus
  for i in range(4):
    newX=x+xbox[i]
    newY=y+ybox[i]
    if 0<=newX<M and 0<=newY<N and l[x][y]>l[newX][newY]:
      if not visited[newX][newY]:
        cnt[newX][newY]+=plus
      else:
        update(newX,newY,plus)

for i in range(M):
  for j in range(N):
    visited[i][j]=True
    if cnt[i][j]==0:
      continue
    for k in range(4):
      newX=i+xbox[k]
      newY=j+ybox[k]
      if 0<=newX<M and 0<=newY<N and l[i][j]>l[newX][newY]:
        if not visited[newX][newY]:
          cnt[newX][newY]+=cnt[i][j]
        else:
          update(newX,newY,cnt[i][j])

print(cnt[M-1][N-1])
