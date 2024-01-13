from collections import deque

def find(N,K):
  q=deque([[N,0]])
  while q:
    [now,cnt]=q.popleft()
    l[now]=True
    if now==K:
      return cnt
    if 0<=now+1<200000 and not l[now+1]:
      q.append([now+1,cnt+1])
    if 0<=now-1<200000 and not l[now-1]:
      q.append([now-1,cnt+1])
    if 0<=now*2<200000 and not l[now*2]:
      q.appendleft([now*2,cnt])

N,K=map(int,input().split())
l=[False for i in range(200000)]

print(find(N,K))
