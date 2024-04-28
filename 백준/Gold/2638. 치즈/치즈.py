import sys
input=sys.stdin.readline

def count():
  time=0
  while len(cheese):
    time+=1
    visited=[[False for i in range(M)]for j in range(N)]
    cnt=[[0 for i in range(M)]for j in range(N)]
    melt={}

    q=[[0,0]]
    while q:
      x,y=q.pop()
      if visited[x][y]:
        continue
      visited[x][y]=True
      for i in range(4):
        newX=x+xbox[i]
        newY=y+ybox[i]
        if 0<=newX<N and 0<=newY<M:
          if newX in cheese and newY in cheese[newX]:
            cnt[newX][newY]+=1
            if cnt[newX][newY]>=2:
              if newX in melt:
                melt[newX][newY]=True
              else:
                melt[newX]={newY:True}
          else:
            q.append([newX,newY])

    for x in melt:
      for y in melt[x]:
        cheese[x].pop(y)
        if not cheese[x]:
          cheese.pop(x)

  print(time)


N,M=map(int,input().split())
cheese={}
for i in range(N):
  now=list(map(int,input().split()))
  for j in range(M):
    if now[j]==1:
      if i in cheese:
        cheese[i][j]=True
      else:
        cheese[i]={j:True}

xbox=[-1,1,0,0]
ybox=[0,0,-1,1]
count()

# 8 9
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 1 1 0 0 0 1 1 0
# 0 1 0 1 1 1 0 1 0
# 0 1 0 0 1 0 0 1 0
# 0 1 0 1 1 1 0 1 0
# 0 1 1 0 0 0 1 1 0
# 0 0 0 0 0 0 0 0 0
