import sys
input=sys.stdin.readline

N,K=map(int,input().split())
l=[]
info={}
for i in range(N):
  now=list(map(int,input().split()))
  for j in range(N):
    if now[j]!=0:
      if now[j] in info:
        info[now[j]].append([i,j])
      else:
        info[now[j]]=[[i,j]]
  l.append(now)
S,X,Y=map(int,input().split())

xbox=[-1,1,0,0]
ybox=[0,0,-1,1]

for _ in range(S):
  newInfo={}
  for i in range(1,K+1):
    if i not in info:
      continue
    for [x,y] in info[i]:
      for j in range(4):
        newX=x+xbox[j]
        newY=y+ybox[j]
        if 0<=newX<N and 0<=newY<N and l[newX][newY]==0:
          l[newX][newY]=i
          if i in newInfo:
            newInfo[i].append([newX,newY])
          else:
            newInfo[i]=[[newX,newY]]
  info=newInfo

print(l[X-1][Y-1])
