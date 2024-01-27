import sys
from collections import deque
input=sys.stdin.readline

# 오른쪽을 보고 있음
# 벽 또는 자기 자신과 만나면 게임 끝
# 몸을 늘려 머리를 다음칸에

def find(N,x,y,d,exist):
  if d=='T':
    for i in range(x,-1,-1):
      if l[i][y]==-1:
        break
      if dir and time[0]==int(dir[0][0]):
        if dir[0][1]=='L':
          dir.popleft()
          find(N,i,y,'L',exist)
        else:
          dir.popleft()
          find(N,i,y,'R',exist)
        return

      time[0]+=1
      if l[i][y]==0:
        [prevX,prevY]=exist.popleft()
        l[prevX][prevY]=0
      exist.append([i,y])
      l[i][y]=-1

  elif d=='D':
    for i in range(x,N):
      if l[i][y]==-1:
        break
      if dir and time[0]==int(dir[0][0]):
        if dir[0][1]=='L':
          dir.popleft()
          find(N,i,y,'R',exist)
        else:
          dir.popleft()
          find(N,i,y,'L',exist)
        return

      time[0]+=1
      if l[i][y]==0:
        [prevX,prevY]=exist.popleft()
        l[prevX][prevY]=0
      exist.append([i,y])
      l[i][y]=-1

  elif d=='L':
    for i in range(y,-1,-1):
      if l[x][i]==-1:
        break
      if dir and time[0]==int(dir[0][0]):
        if dir[0][1]=='L':
          dir.popleft()
          find(N,x,i,'D',exist)
        else:
          dir.popleft()
          find(N,x,i,'T',exist)
        return

      time[0]+=1
      if l[x][i]==0:
        [prevX,prevY]=exist.popleft()
        l[prevX][prevY]=0
      exist.append([x,i])
      l[x][i]=-1

  else: # R
    for i in range(y,N):
      if l[x][i]==-1:
        break
      if dir and time[0]==int(dir[0][0]):
        if dir[0][1]=='L':
          dir.popleft()
          find(N,x,i,'T',exist)
        else:
          dir.popleft()
          find(N,x,i,'D',exist)
        return

      time[0]+=1
      if l[x][i]==0:
        [prevX,prevY]=exist.popleft()
        l[prevX][prevY]=0
      exist.append([x,i])
      l[x][i]=-1

  return

N=int(input())
K=int(input())
l=[[0 for i in range(N)]for j in range(N)]

for i in range(K):
  a,b=map(int,input().split())
  l[a-1][b-1]=1

L=int(input()) # 방향 전환 횟수
dir=deque([])
for i in range(L):
  dir.append(list(input().split()))

time=[0]
find(N,0,0,'R',deque([[0,0]]))
print(time[0])
