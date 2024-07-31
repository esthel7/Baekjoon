import sys
from collections import deque
input=sys.stdin.readline

def update(node,prev,cnt):
  info[node][prev]=cnt
  for i in range(1,n+1):
    if info[prev][i]<cnt:
      info[node][i]=info[prev][i]+1


def find():
  q=deque([])
  for i in range(1,n+1):
    if order[i]==0:
      q.append([i,0,i])
      info[i][i]=0

  while q:
    idx,cnt,r=q.popleft()
    for node in link[idx]:
      order[node]-=1
      update(node,idx,cnt+1)
      if order[node]==0:
        q.append([node,cnt+1,idx])



n,k=map(int,input().split())
order=[-1 for i in range(n+1)]
link=[[]for i in range(n+1)]
for i in range(k):
  a,b=map(int,input().split()) # 전, 후
  if order[a]==-1:
    order[a]=0
  if order[b]==-1:
    order[b]=0
  order[b]+=1
  link[a].append(b)

info=[[n+1 for i in range(n+1)] for j in range(n+1)]
find()

# print(info)
s=int(input())
for _ in range(s):
  a,b=map(int,input().split())
  if info[a][b]==n+1 and info[b][a]==n+1:
    print(0)
  elif info[a][b]<n+1:
    print(1)
  else:
    print(-1)

# 7 5
# 1 2
# 1 3
# 3 4
# 2 5
# 6 7
# 20
# 1 4
# 1 5
# 4 5
# 2 3
# 2 4
# 3 5
# 1 6
# 1 7

# -1, -1, 0, 0, 0, 0, 0, 0

# ---

# 5 3
# 1 2
# 3 4
# 1 4
# 20
# 1 4
# 1 3
# 2 3
# 2 4

# -1, 0, 0, 0
