import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

def find(x,y,now):
  global answer
  if answer<now:
    answer=now

  move=int(l[x][y])
  xbox=[-move,move,0,0]
  ybox=[0,0,-move,move]
  for i in range(4):
    newX=x+xbox[i]
    newY=y+ybox[i]
    if 0<=newX<N and 0<=newY<M and l[newX][newY]!='H' and cnt[newX][newY]<now+1:
      if visited[newX][newY]:
        print(-1)
        exit(0)
      visited[newX][newY]=True
      prev=cnt[newX][newY]
      cnt[newX][newY]=now+1
      find(newX,newY,now+1)
      visited[newX][newY]=False


N,M=map(int,input().split())
l=[]
for i in range(N):
  l.append(list(input().rstrip()))

answer=1
visited=[[False for i in range(M)]for j in range(N)]
cnt=[[0 for i in range(M)]for j in range(N)]
find(0,0,1)
print(answer)
