import sys
input=sys.stdin.readline

N,M=map(int,input().split())
l=[]
info={}
for i in range(M):
  x,y,a,b=map(int,input().split())
  if x in info:
    if y in info[x]:
      info[x][y].append([a,b])
    else:
      info[x][y]=[[a,b]]
  else:
    info[x]={y:[[a,b]]}

xbox=[-1,1,0,0]
ybox=[0,0,-1,1]
possible=[[False for i in range(N+1)]for j in range(N+1)]
possible[1][1]=True
visited=[[False for i in range(N+1)]for j in range(N+1)]
visited[1][1]=True
answer=1

q=[[1,1]] # 이동 가능하고 불 켜진 방만
while q:
  x,y=q.pop()
  if x in info and y in info[x]:
    for [tx,ty] in info[x][y]:
      if not possible[tx][ty]:
        possible[tx][ty]=True
        answer+=1
        for i in range(4):
          mx=tx+xbox[i]
          my=ty+ybox[i]
          if 0<mx<=N and 0<my<=N and visited[mx][my]:
            visited[tx][ty]=True
            q.append([tx,ty])
            break

  for i in range(4):
    newX=x+xbox[i]
    newY=y+ybox[i]
    if 0<newX<=N and 0<newY<=N and possible[newX][newY] and not visited[newX][newY]:
      visited[newX][newY]=True
      q.append([newX,newY])

print(answer)
