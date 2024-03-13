import sys
from collections import deque
input=sys.stdin.readline

def find(N):
  visited=[[-1 for i in range(N)]for j in range(N)]
  visited[0][0]=l[0][0]
  q=deque([[0,0]])
  answer=-1
  while q:
    x,y=q.popleft()
    now=visited[x][y]
    if answer!=-1 and answer<=now:
      continue
    if x==N-1 and y==N-1:
      if answer==-1:
        answer=now
      elif answer>now:
        answer=now
      continue
    for i in range(4):
      newX=x+xbox[i]
      newY=y+ybox[i]
      if 0<=newX<N and 0<=newY<N and (visited[newX][newY]==-1 or (visited[newX][newY]!=-1 and visited[newX][newY]>now+l[newX][newY])):
        visited[newX][newY]=now+l[newX][newY]
        q.append([newX,newY])

  return answer

xbox=[-1,1,0,0]
ybox=[0,0,-1,1]
test=0
while True:
  N=int(input())
  if N==0:
    break
  test+=1
  l=[]
  for i in range(N):
    l.append(list(map(int,input().split())))
  print('Problem %d: '%(test),end='')
  print(find(N))
