import sys
from collections import deque
input=sys.stdin.readline

# 로봇 올리거나 이동하면 칸의 내구도는 1만큼 감소

N,K=map(int,input().split())
l=deque(list(map(int,input().split())))

now=deque([])
cnt=0
time=1
while True:
  last=l.pop()
  l.appendleft(last)

  L=len(now)
  for i in range(L-1,-1,-1):
    now[i]+=1
    if now[i]==N-1:
      now.pop()
      continue
    if l[now[i]+1]>0 and ((i+1<len(now) and now[i+1]!=now[i]+1) or i==len(now)-1):
      now[i]+=1
      l[now[i]]-=1
      if l[now[i]]==0:
        cnt+=1
      if now[i]==N-1:
        now.pop()

  if last!=0:
    l[0]-=1
    if l[0]==0:
      cnt+=1
    now.appendleft(0)

  if cnt>=K:
    print(time)
    exit(0)

  time+=1
