import sys
from collections import deque
import copy
input=sys.stdin.readline

door={'A':'a','B':'b','C':'c','D':'d','E':'e','F':'f'}
key={'a':True,'b':True,'c':True,'d':True,'e':True,'f':True}
changeNum={'a':1,'b':2,'c':4,'d':8,'e':16,'f':32}

N,M=map(int,input().split())
l=[]
x=-1
y=-1
for i in range(N):
  now=list(input().rstrip())
  if x==-1:
    for j in range(M):
      if now[j]=='0':
        now[j]='.'
        x=i
        y=j
        break
  l.append(now)

xbox=[-1,1,0,0]
ybox=[0,0,-1,1]

q=deque([[x,y,0,0,{}]])
visited=[[[False for i in range(M)]for j in range(N)]for k in range(64)]
visited[0][x][y]=True
while q:
  x,y,cnt,now,keys=q.popleft()
  for i in range(4):
    newX=x+xbox[i]
    newY=y+ybox[i]
    if 0<=newX<N and 0<=newY<M and l[newX][newY]!='#':
      if l[newX][newY]=='1':
        print(cnt+1)
        exit(0)
      if l[newX][newY]=='.':
        if not visited[now][newX][newY]:
          visited[now][newX][newY]=True
          q.append([newX,newY,cnt+1,now,keys])
      elif l[newX][newY] in key:
        if l[newX][newY] not in keys:
          newKeys=copy.deepcopy(keys)
          newKeys[l[newX][newY]]=True
          now+=changeNum[l[newX][newY]]
          if not visited[now][newX][newY]:
            visited[now][newX][newY]=True
            q.append([newX,newY,cnt+1,now,newKeys])
          now-=changeNum[l[newX][newY]]
        else:
          if not visited[now][newX][newY]:
            visited[now][newX][newY]=True
            q.append([newX,newY,cnt+1,now,keys])
      elif l[newX][newY] in door and door[l[newX][newY]] in keys:
        if not visited[now][newX][newY]:
          visited[now][newX][newY]=True
          q.append([newX,newY,cnt+1,now,keys])

print(-1)

# 6 6
# a#AAA1
# .#B###
# .#A###
# 0.....
# #####b
# #####a
