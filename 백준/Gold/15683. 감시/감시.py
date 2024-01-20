import sys
input=sys.stdin.readline

def go(l,N,M,x,y,dir):
  if dir=='UP':
    for i in range(x,-1,-1):
      if l[i][y]==6:
        break
      if l[i][y]==0:
        l[i][y]=-1
  elif dir=='DOWN':
    for i in range(x,N):
      if l[i][y]==6:
        break
      if l[i][y]==0:
        l[i][y]=-1
  elif dir=='LEFT':
    for i in range(y,-1,-1):
      if l[x][i]==6:
        break
      if l[x][i]==0:
        l[x][i]=-1
  else:
    for i in range(y,M):
      if l[x][i]==6:
        break
      if l[x][i]==0:
        l[x][i]=-1

def make(l,N,M,x,y,num,now):
  if num==1:
    if now==0:
      go(l,N,M,x,y,'UP')
    elif now==1:
      go(l,N,M,x,y,'DOWN')
    elif now==2:
      go(l,N,M,x,y,'LEFT')
    else:
      go(l,N,M,x,y,'RIGHT')
  elif num==2:
    if now==0:
      go(l,N,M,x,y,'UP')
      go(l,N,M,x,y,'DOWN')
    else:
      go(l,N,M,x,y,'LEFT')
      go(l,N,M,x,y,'RIGHT')
  elif num==3:
    if now==0:
      go(l,N,M,x,y,'UP')
      go(l,N,M,x,y,'RIGHT')
    elif now==1:
      go(l,N,M,x,y,'DOWN')
      go(l,N,M,x,y,'RIGHT')
    elif now==2:
      go(l,N,M,x,y,'DOWN')
      go(l,N,M,x,y,'LEFT')
    else:
      go(l,N,M,x,y,'UP')
      go(l,N,M,x,y,'LEFT')
  elif num==4:
    if now==0:
      go(l,N,M,x,y,'UP')
      go(l,N,M,x,y,'DOWN')
      go(l,N,M,x,y,'LEFT')
    elif now==1:
      go(l,N,M,x,y,'UP')
      go(l,N,M,x,y,'DOWN')
      go(l,N,M,x,y,'RIGHT')
    elif now==2:
      go(l,N,M,x,y,'UP')
      go(l,N,M,x,y,'LEFT')
      go(l,N,M,x,y,'RIGHT')
    else:
      go(l,N,M,x,y,'DOWN')
      go(l,N,M,x,y,'LEFT')
      go(l,N,M,x,y,'RIGHT')
  else:
    go(l,N,M,x,y,'UP')
    go(l,N,M,x,y,'DOWN')
    go(l,N,M,x,y,'LEFT')
    go(l,N,M,x,y,'RIGHT')
  return list([list(arr) for arr in l])


def calculate(l,N,M):
  now=0
  for i in range(N):
    for j in range(M):
      if l[i][j]==0:
        now+=1
  if total[0]==-1 or total[0]>now:
    total[0]=now


def find(l,N,M,idx):
  if idx==len(cctv):
    calculate(l,N,M)
    return

  [x,y,cctvNum]=cctv[idx]
  for i in range(info[cctvNum]):
    first=list([list(arr) for arr in l])
    first=make(first,N,M,x,y,cctvNum,i)
    find(first,N,M,idx+1)


N,M=map(int,input().split())
l=[]
for i in range(N):
  l.append(list(map(int,input().split())))

cctv=[]
for i in range(N):
  for j in range(M):
    if l[i][j]>0 and l[i][j]!=6:
      cctv.append([i,j,l[i][j]])

info={
  1:4,
  2:2,
  3:4,
  4:4,
  5:1
}
total=[-1]
find(l,N,M,0)
print(total[0])
