from collections import deque

def left(s,idx):
  for i in range(idx):
    a=s.popleft()
    s.append(a)
  s.popleft()

def right(s,idx):
  for i in range(idx):
    a=s.pop()
    s.appendleft(a)
  s.popleft()

N,M=map(int,input().split())
l=list(map(int,input().split()))
s=deque()
for i in range(1,N+1):
  s.append(i)

cnt=0
for i in range(M):
  now=l[i]
  total=len(s)
  for j in range(total):
    if s[j]==now:
      if j<total-j: # left
        left(s,j)
        cnt+=j
      else:
        right(s,total-j)
        cnt+=total-j
      break
print(cnt)
