import sys
input=sys.stdin.readline

N,L=map(int,input().split())
l=[]
for i in range(N):
  l.append(list(map(int,input().split())))

cnt=0
# 가로
for i in range(N):
  j=1
  breakFlag=False
  road=[False for k in range(N)]

  while j!=N:
    if l[i][j-1]==l[i][j]:
      j+=1
    elif l[i][j-1]==l[i][j]-1: # 오르막길
      if j-L>=0:
        first=l[i][j-1]
        for k in range(j-1,j-1-L,-1):
          if l[i][k]!=first or road[k]:
            breakFlag=True
            break
        if breakFlag:
          break
        for k in range(j-1,j-1-L,-1):
          road[k]=True
        j+=1
      else:
        breakFlag=True
        break
    elif l[i][j-1]==l[i][j]+1: # 내리막길
      if j-1+L<N:
        first=l[i][j]
        for k in range(j,j+L):
          if l[i][k]!=first or road[k]:
            breakFlag=True
            break
        if breakFlag:
          break
        for k in range(j,j+L):
          road[k]=True
        j+=L
      else:
        breakFlag=True
        break
    else:
      breakFlag=True
      break

  if breakFlag:
    continue
  cnt+=1

# 세로
for i in range(N):
  j=1
  breakFlag=False
  road=[False for k in range(N)]

  while j!=N:
    if l[j-1][i]==l[j][i]:
      j+=1
    elif l[j-1][i]==l[j][i]-1: # 오르막길
      if j-L>=0:
        first=l[j-1][i]
        for k in range(j-1,j-1-L,-1):
          if l[k][i]!=first or road[k]:
            breakFlag=True
            break
        if breakFlag:
          break
        for k in range(j-1,j-1-L,-1):
          road[k]=True
        j+=1
      else:
        breakFlag=True
        break
    elif l[j-1][i]==l[j][i]+1: # 내리막길
      if j-1+L<N:
        first=l[j][i]
        for k in range(j,j+L):
          if l[k][i]!=first or road[k]:
            breakFlag=True
            break
        if breakFlag:
          break
        for k in range(j,j+L):
          road[k]=True
        j+=L
      else:
        breakFlag=True
        break
    else:
      breakFlag=True
      break

  if breakFlag:
    continue
  cnt+=1

print(cnt)
