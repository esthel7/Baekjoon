import sys
from collections import deque
input=sys.stdin.readline

def check(fx,fy,sx,sy,N,M):
  if (fx==0 and sx!=0) or (fx!=0 and sx==0) or (fx==N-1 and sx!=N-1) or (fx!=N-1 and sx==N-1) or (fy==0 and sy!=0) or (fy!=0 and sy==0) or (fy==M-1 and sy!=M-1) or (fy!=M-1 and sy==M-1):
    return True
  return False

def find(N,M):
  q=deque([[coin[0][0],coin[0][1],coin[1][0],coin[1][1],1]])
  if check(coin[0][0],coin[0][1],coin[1][0],coin[1][1],N,M):
    print(1)
    return

  while q:
    [fx,fy,sx,sy,cnt]=q.popleft()
    for i in range(4):
      nfx=fx+xbox[i]
      nfy=fy+ybox[i]
      nsx=sx+xbox[i]
      nsy=sy+ybox[i]

      if 0<=nfx<N and 0<=nfy<M and 0<=nsx<N and 0<=nsy<M:
        if l[nfx][nfy]!='#':
          if l[nsx][nsy]!='#':
            if check(nfx,nfy,nsx,nsy,N,M):
              print(cnt+1)
              return
            if cnt==9:
              continue
            q.append([nfx,nfy,nsx,nsy,cnt+1])
          else:
            if check(nfx,nfy,sx,sy,N,M):
              print(cnt+1)
              return
            if cnt==9:
              continue
            q.append([nfx,nfy,sx,sy,cnt+1])
        else:
          if l[nsx][nsy]!='#':
            if check(fx,fy,nsx,nsy,N,M):
              print(cnt+1)
              return
            if cnt==9:
              continue
            q.append([fx,fy,nsx,nsy,cnt+1])

  print(-1)

N,M=map(int,input().split())
l=[]
coin=[]
for i in range(N):
  a=list(input().rstrip())
  for j in range(M):
    if a[j]=='o':
      coin.append([i,j])
  l.append(a)

xbox=[-1,1,0,0]
ybox=[0,0,-1,1]
find(N,M)
