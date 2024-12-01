import sys
from collections import deque
input=sys.stdin.readline

N,M=map(int,input().split())
l=[]
for i in range(N):
  l.append(list(map(int,input().split())))

ybox=[-1,0,1]
visited=[[[-1 for i in range(M)]for j in range(N)]for k in range(3)]

q=deque([])
for i in range(M):
  for j in range(3):
    newY=i+ybox[j]
    if 0<=newY<M:
      visited[j][1][newY]=l[0][i]
      q.append([j,1,newY])

answer=-1
while q:
  num,x,y=q.popleft()
  if x+1==N:
    value=visited[num][x][y]+l[x][y]
    if answer==-1 or answer>value:
      answer=value
    continue
  for i in range(3):
    if i==num:
      continue
    newY=y+ybox[i]
    if 0<=newY<M and (visited[i][x+1][newY]==-1 or visited[i][x+1][newY]>visited[num][x][y]+l[x][y]):
      visited[i][x+1][newY]=visited[num][x][y]+l[x][y]
      q.append([i,x+1,newY])

print(answer)
