import sys
from collections import deque
iput=sys.stdin.readline

# 100 넘어가면 이동 불가
# 사다리면 사다리타고 위로 올라가기
# 뱀이면 뱀 따라 내려가기

N,M=map(int,input().split())
info={}
for i in range(N):
  x,y=map(int,input().split())
  info[x]=y

for i in range(M):
  u,v=map(int,input().split())
  info[u]=v

visited=[False for i in range(101)]
visited[1]=True
q=deque([[1,0]])
while q:
  idx,cnt=q.popleft()
  if idx==100:
    print(cnt)
    break
  for i in range(1,7):
    if idx+i>100:
      break
    if visited[idx+i]:
      continue
    visited[idx+i]=True
    if idx+i in info:
      if visited[info[idx+i]]:
        continue
      visited[info[idx+i]]=True
      q.append([info[idx+i],cnt+1])
    else:
      q.append([idx+i,cnt+1])

