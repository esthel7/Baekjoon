import sys
from collections import deque
input=sys.stdin.readline

def best(x,y,total):
  answer=[-1,-1]
  visited=[[False for i in range(N)]for j in range(N)]
  visited[x][y]=True
  q=deque([[x,y,0]])
  while q:
    x,y,cnt=q.popleft()
    if total<cnt:
      print(-1)
      exit(0)
    if answer[0]!=-1 and answer[0]<cnt:
      break
    if x in person and y in person[x]:
      if answer[0]==-1:
        answer=[cnt,person[x][y]]
      elif answer[0]==cnt:
        prev=loc[answer[1]]
        now=loc[person[x][y]]
        if prev[0]>now[0] or (prev[0]==now[0] and prev[1]>now[1]):
          answer=[cnt,person[x][y]]
      continue
    for i in range(4):
      newX=x+xbox[i]
      newY=y+ybox[i]
      if 0<=newX<N and 0<=newY<N and l[newX][newY]!=1 and not visited[newX][newY]:
        visited[newX][newY]=True
        q.append([newX,newY,cnt+1])

  if answer[0]==-1:
    print(-1)
    exit(0)
  return answer


def move(idx,total):
  startx,starty=loc[idx]
  visited=[[False for i in range(N)]for j in range(N)]
  visited[startx][starty]=True
  q=deque([[startx,starty,0]])
  while q:
    x,y,cnt=q.popleft()
    if cnt>total:
      print(-1)
      exit(0)
    if x==end[idx][0] and y==end[idx][1]:
      return total+cnt
    for i in range(4):
      newX=x+xbox[i]
      newY=y+ybox[i]
      if 0<=newX<N and 0<=newY<N and l[newX][newY]!=1 and not visited[newX][newY]:
        visited[newX][newY]=True
        q.append([newX,newY,cnt+1])
  print(-1)
  exit(0)


def find(x,y,total):
  if not len(loc):
    print(total)
    exit(0)

  [cnt,idx]=best(x,y,total)
  cnt=move(idx,total-cnt)
  px,py=loc[idx]
  person[px].pop(py)
  if not len(person[px]):
    person.pop(px)
  nextx,nexty=end[idx]
  loc.pop(idx)
  end.pop(idx)
  find(nextx,nexty,cnt)


N,M,First=map(int,input().split())

l=[]
for i in range(N):
  l.append(list(map(int,input().split())))

startx,starty=map(int,input().split())

loc={}
end={}
person={}
for i in range(M):
  x,y,X,Y=map(int,input().split())
  loc[i]=[x-1,y-1]
  end[i]=[X-1,Y-1]
  if x-1 in person:
    person[x-1][y-1]=i
  else:
    person[x-1]={y-1:i}

xbox=[-1,1,0,0]
ybox=[0,0,-1,1]
find(startx-1,starty-1,First)
