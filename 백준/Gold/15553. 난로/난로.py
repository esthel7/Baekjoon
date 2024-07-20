import sys
from collections import deque
input=sys.stdin.readline

def update(idx,time,cnt,value):
  if time in dp[idx]:
    if cnt in dp[idx][time]:
      dp[idx][time][cnt][value]=True
    else:
      dp[idx][time][cnt]={value:True}
  else:
    dp[idx][time]={cnt:{value:True}}

N,K=map(int,input().split())

l=deque([])
for i in range(N):
  l.append(int(input()))

last=l[-1]+1
dp=[{} for i in range(last)]
dp[0]={0:{0:{False:True}}}
for i in range(last-1):
  if l and l[0]==i:
    l.popleft()
    for time in dp[i].keys():
      for cnt in dp[i][time].keys():
        for value in dp[i][time][cnt].keys():
          if value:
            update(i+1,time+1,cnt,True)
          else:
            if cnt+1<=K:
              update(i+1,time+1,cnt+1,True)
  else:
    for time in dp[i].keys():
      for cnt in dp[i][time].keys():
        for value in dp[i][time][cnt].keys():
          if value:
            update(i+1,time+1,cnt,True)
            if cnt+1<=K:
              update(i+1,time,cnt,False)
          else:
            update(i+1,time,cnt,False)
  dp[i]={}

answer=last
for time in dp[last-1].keys():
  answer=min(time,answer)
print(answer+1)
