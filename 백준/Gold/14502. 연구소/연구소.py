import sys
input=sys.stdin.readline

def calculate(now):
  global answer
  cnt=P-3
  l=list(list(arr)for arr in board)
  visited=[[False for i in range(M)]for j in range(N)]

  for i in range(N):
    for j in range(M):
      if l[i][j]==2 and not visited[i][j]:
        visited[i][j]=True

        q=[[i,j]]
        while q:
          x,y=q.pop()
          for k in range(4):
            newX=x+xbox[k]
            newY=y+ybox[k]
            if 0<=newX<N and 0<=newY<M and not visited[newX][newY]:
              visited[newX][newY]=True
              if l[newX][newY] in [0,2] and [newX,newY] not in now:
                if l[newX][newY]==0:
                  cnt-=1
                q.append([newX,newY])
  
  if answer<cnt:
    answer=cnt


def find(now,start):
  if len(now)==3:
    calculate(now)
    return
  for i in range(start,P):
    now.append(possible[i])
    find(now,i+1)
    now.pop()

N,M=map(int,input().split())
board=[]
possible=[]
for i in range(N):
  now=list(map(int,input().split()))
  board.append(now)
  for j in range(M):
    if now[j]==0:
      possible.append([i,j])

answer=0
xbox=[-1,1,0,0]
ybox=[0,0,-1,1]
P=len(possible)
find([],0)
print(answer)
