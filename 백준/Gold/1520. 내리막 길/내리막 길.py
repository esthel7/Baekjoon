import sys
input=sys.stdin.readline

# 상하좌우 이웃한 곳끼리 이동 가능
# 왼쪽 위에서 오른쪽 아래로 이동
# 높이가 더 낮은 지점으로만 이동

def update(x,y,plus):
  for i in range(4):
    newX=x+xbox[i]
    newY=y+ybox[i]
    if 0<=newX<M and 0<=newY<N and l[newX][newY]<l[x][y]:
      cnt[newX][newY]+=plus
      if visited[newX][newY]:
        update(newX,newY,plus)


M,N=map(int,input().split())
l=[]
for i in range(M):
  l.append(list(map(int,input().split())))

cnt=[[0 for i in range(N)]for i in range(M)]
cnt[0][0]=1

visited=[[False for i in range(N)]for j in range(M)]
visited[0][0]=True

xbox=[-1,1,0,0]
ybox=[0,0,-1,1]

for x in range(M):
  for y in range(N):
    visited[x][y]=True
    if cnt[x][y]==0:
      continue
    update(x,y,cnt[x][y])

print(cnt[M-1][N-1])
