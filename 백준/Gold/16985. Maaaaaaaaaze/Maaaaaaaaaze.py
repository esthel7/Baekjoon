import sys
from collections import deque
input=sys.stdin.readline

def clock(nowL):
  newL=[]
  for i in range(5):
    newL.append([])
    for j in range(4,-1,-1):
      newL[i].append(nowL[j][i])
  return list(list(arr) for arr in newL)


def find(num,rotate):
  visit=[[[-1 for i in range(5)]for j in range(5)]for k in range(5)]
  q=deque([[0,0,0,0]])
  visit[num[0]][0][0]=0

  while q:
    [idx,x,y,cnt]=q.popleft()
    floor=num[idx] # 층
    nowL=l[floor][rotate[idx]]

    if x==4 and y==4 and idx==4:
      if answer[0]==-1:
        answer[0]=cnt
      else:
        answer[0]=min(answer[0],cnt)
      return

    if idx+1<5:
      nextL=l[num[idx+1]][rotate[idx+1]]
      if nextL[x][y]==1 and (visit[num[idx+1]][x][y]==-1 or visit[num[idx+1]][x][y]>cnt+1):
        visit[num[idx+1]][x][y]=cnt+1
        q.append([idx+1,x,y,cnt+1])

    for i in range(4):
      newX=x+xbox[i]
      newY=y+ybox[i]
      if 0>newX or newX>=5 or 0>newY or newY>=5:
        continue
      if nowL[newX][newY]==1 and (visit[floor][newX][newY]==-1 or visit[floor][newX][newY]>cnt+1):
        visit[floor][newX][newY]=cnt+1
        q.append([idx,newX,newY,cnt+1])
  
    if idx-1>=0:
      prevL=l[num[idx-1]][rotate[idx-1]]
      if prevL[x][y]==1 and (visit[num[idx-1]][x][y]==-1 or visit[num[idx-1]][x][y]>cnt+1):
        visit[num[idx-1]][x][y]=cnt+1
        q.append([idx-1,x,y,cnt+1])


def possible(nowL,num,idx,rotate):
  if idx==0 and nowL[0][0]!=1:
    return
  if idx==4:
    if nowL[4][4]!=1:
      return
    if answer[0]!=12:
      find(num,rotate)
  else:
    for i in range(4):
      rotate.append(i)
      possible(l[num[idx+1]][i],num,idx+1,rotate)
      rotate.pop()


def make(num):
  if len(num)==5:
    for i in range(4):
      possible(l[num[0]][i],num,0,[i])
    return

  for i in range(5):
    if i in num:
      continue
    num.append(i)
    make(num)
    num.pop()


first=[]
for i in range(5):
  first.append([])
  for j in range(5):
    first[i].append(list(map(int,input().split())))

l=[]
for i in range(5):
  l.append([])
  nowL=list(list(arr) for arr in first[i])
  l[i].append(nowL)
  for j in range(3):
    nowL=clock(nowL)
    l[i].append(nowL)

xbox=[-1,1,0,0]
ybox=[0,0,-1,1]
answer=[-1]
make([])
print(answer[0])
