import sys
input=sys.stdin.readline

N=int(input())
l=[]
for i in range(N):
  l.append(list(map(int,input().split())))

Min=100
Max=1
for i in range(N):
  mins=min(l[i])
  maxs=max(l[i])
  if Min>mins:
    Min=mins
  if Max<maxs:
    Max=maxs

def find(x,y,N,t):
  xbox=[-1,1,0,0]
  ybox=[0,0,-1,1]
  q=[[x,y]]
  cnt=0
  while q:
    [x,y]=q.pop()
    if x<0 or y<0 or x>=N or y>=N:
      continue
    if visit[x][y]==t or l[x][y]<=t:
      continue
    visit[x][y]=t
    cnt+=1
    for i in range(4):
      q.append([x+xbox[i],y+ybox[i]])


answer=1
for t in range(Min,Max):
  visit=[[200 for i in range(N)]for j in range(N)]
  cnt=0
  for i in range(N):
    for j in range(N):
      if l[i][j]>t and visit[i][j]>t:
        find(i,j,N,t)
        cnt+=1
  if answer<cnt:
    answer=cnt
print(answer)
