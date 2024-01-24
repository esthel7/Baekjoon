import sys
from collections import deque
input=sys.stdin.readline

def move(N,now,idx):
  now=list(list(arr) for arr in now)

  if idx==0: # 상
    for i in range(N):
      last=0
      for j in range(N):
        if now[j][i]==0:
          continue
        else:
          if last!=j:
            now[last][i]=now[j][i]
            now[j][i]=0
          last+=1

      for j in range(1,N):
        if now[j][i]==now[j-1][i] and now[j][i]!=0:
          now[j-1][i]*=2
          for k in range(j,N-1):
            now[k][i]=now[k+1][i]
            if now[k+1][i]==0:
              break
          now[N-1][i]=0

  elif idx==1: # 하
    for i in range(N-1,-1,-1):
      last=N-1
      for j in range(N-1,-1,-1):
        if now[j][i]==0:
          continue
        else:
          if last!=j:
            now[last][i]=now[j][i]
            now[j][i]=0
          last-=1

      for j in range(N-2,-1,-1):
        if now[j][i]==now[j+1][i] and now[j][i]!=0:
          now[j+1][i]*=2
          for k in range(j,0,-1):
            now[k][i]=now[k-1][i]
            if now[k-1][i]==0:
              break
          now[0][i]=0

  elif idx==2: # 좌
    for i in range(N):
      last=0
      for j in range(N):
        if now[i][j]==0:
          continue
        else:
          if last!=j:
            now[i][last]=now[i][j]
            now[i][j]=0
          last+=1

      for j in range(1,N):
        if now[i][j]==now[i][j-1] and now[i][j]!=0:
          now[i][j-1]*=2
          for k in range(j,N-1):
            now[i][k]=now[i][k+1]
            if now[i][k+1]==0:
              break
          now[i][N-1]=0

  else: # 우
    for i in range(N-1,-1,-1):
      last=N-1
      for j in range(N-1,-1,-1):
        if now[i][j]==0:
          continue
        else:
          if last!=j:
            now[i][last]=now[i][j]
            now[i][j]=0
          last-=1

      for j in range(N-2,-1,-1):
        if now[i][j]==now[i][j+1] and now[i][j]!=0:
          now[i][j+1]*=2
          for k in range(j,0,-1):
            now[i][k]=now[i][k-1]
            if now[i][k-1]==0:
              break
          now[i][0]=0

  return now


def find(N):
  q=deque([[list(l),0]])
  while q:
    [now,cnt]=q.popleft()
    if cnt==5:
      Max=0
      for i in range(N):
        MaxValue=max(now[i])
        if Max<MaxValue:
          Max=MaxValue
      if final[0]<Max:
        final[0]=Max
      continue

    for i in range(4):
      newL=move(N,now,i)
      q.append([list(list(arr) for arr in newL),cnt+1])


N=int(input())
l=[]
for i in range(N):
  l.append(list(map(int,input().split())))

final=[0]
find(N)
print(final[0])
