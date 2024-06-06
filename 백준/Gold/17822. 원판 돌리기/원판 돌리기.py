import sys
input=sys.stdin.readline

def sameCheck(x):
  global change
  for i in range(M):
    value=l[x][i]
    if value==0:
      continue
    changeFlag=False
    for j in range(x-1,-1,-1):
      if value==l[j][i]:
        changeFlag=True
      else:
        break
    for j in range(x+1,N):
      if value==l[j][i]:
        changeFlag=True
      else:
        break
    if changeFlag:
      if x in change:
        change[x][i]=True
      else:
        change[x]={i:True}

  for i in range(1,M):
    if l[x][i]==l[x][i-1] and l[x][i]!=0:
      if x in change:
        change[x][i]=True
        change[x][i-1]=True
      else:
        change[x]={i:True,i-1:True}
  if l[x][0]==l[x][M-1] and l[x][0]!=0:
    if x in change:
      change[x][0]=True
      change[x][M-1]=True
    else:
      change[x]={0:True,M-1:True}


def calculate():
  global change
  change={}
  for i in range(N):
    sameCheck(i)
  
  if len(change):
    for x in change:
      for y in change[x]:
        l[x][y]=0
  else:

    total=0
    cnt=0
    for i in range(N):
      for j in range(M):
        if l[i][j]!=0:
          cnt+=1
          total+=l[i][j]
    if cnt!=0:
      ave=total/cnt
      for i in range(N):
        for j in range(M):
          if l[i][j]==0:
            continue
          if l[i][j]>ave:
            l[i][j]-=1
          elif l[i][j]<ave:
            l[i][j]+=1


def clock(x,k):
  global l
  tmp=list(l[x])
  left=tmp[:k]
  right=tmp[k:]
  l[x]=right+left


N,M,T=map(int,input().split())
l=[]
for i in range(N):
  l.append(list(map(int,input().split())))

change={}
for i in range(T):
  x,d,k=map(int,input().split())
  if d==0:
    k=M-k
  for j in range(x-1,N,x):
    clock(j,k)
  calculate()

total=0
for i in range(N):
  for j in range(M):
    total+=l[i][j]

print(total)
