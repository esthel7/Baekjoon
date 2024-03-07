import sys
input=sys.stdin.readline

# 등장 횟수 작은것부터, 수 작은 것부터

def R(maxG,maxS):
  global l
  for i in range(maxS):
    infoL={}
    for j in range(maxG):
      if l[i][j]==0:
        continue
      if l[i][j] in infoL:
        infoL[l[i][j]]+=1
      else:
        infoL[l[i][j]]=1
      l[i][j]=0
    newL=[]
    for keys in infoL.keys():
      newL.append([infoL[keys],keys])
    newL.sort()

    for j in range(len(newL)):
      l[i][j*2]=newL[j][1]
      l[i][j*2+1]=newL[j][0]

    if maxG<len(newL)*2:
      maxG=len(newL)*2

  return [maxG,maxS]


def C(maxG,maxS):
  global l
  for i in range(maxG):
    infoL={}
    for j in range(maxS):
      if l[j][i]==0:
        continue
      if l[j][i] in infoL:
        infoL[l[j][i]]+=1
      else:
        infoL[l[j][i]]=1
      l[j][i]=0

    newL=[]
    for keys in infoL.keys():
      newL.append([infoL[keys],keys])
    newL.sort()

    for j in range(len(newL)):
      l[j*2][i]=newL[j][1]
      l[j*2+1][i]=newL[j][0]

    if maxS<len(newL)*2:
      maxS=len(newL)*2

  return [maxG,maxS]



r,c,k=map(int,input().split())
r-=1
c-=1
l=[[0 for i in range(300)]for j in range(300)]

for i in range(3):
  now=list(map(int,input().split()))
  for j in range(3):
    l[i][j]=now[j]

maxG=3
maxS=3
time=0
while True:
  if maxS>r and maxG>c and l[r][c]==k:
    print(time)
    break
  if time==100:
    print(-1)
    break
  time+=1

  if maxS>=maxG:
    [maxG,maxS]=R(maxG,maxS)
  else:
    [maxG,maxS]=C(maxG,maxS)
  
  # print()
  # for i in range(maxS):
  #   for j in range(maxG):
  #     print(l[i][j],end=' ')
  #   print()
  # print('time=',time,'maxG',maxG,'maxS',maxS)
