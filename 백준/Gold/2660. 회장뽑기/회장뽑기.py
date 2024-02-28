import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
f=[[55 for i in range(n)]for j in range(n)]

for i in range(n):
  f[i][i]=0

while True:
  a,b=map(int,input().split())
  if a==-1:
    break
  a-=1
  b-=1

  f[a][b]=1
  f[b][a]=1

q=deque([i for i in range(n)])
while q:
  i=q.popleft()
  s=[]
  for j in range(n):
    if i==j:
      continue
    if f[i][j]!=55:
      s.append(j)

  for sValue in s:
    plusFlag=False
    for item in s:
      value=f[i][sValue]+f[i][item]
      if sValue==item:
        continue
      if f[sValue][item]>value:
        f[sValue][item]=value
        f[item][sValue]=value
        plusFlag=True
    if plusFlag:
      q.append(sValue)

Min=55
for i in range(n):
  now=max(f[i])
  if Min>now:
    Min=now
    l=[i]
  elif Min==now:
    l.append(i)

print(Min,len(l))
for answer in l:
  print(answer+1,end=' ')
