import sys
from collections import deque
input=sys.stdin.readline

N=int(input())

month=[0 for i in range(13)]
month[1]=31
month[2]=28
month[3]=31
month[4]=30
month[5]=31
month[6]=30
month[7]=31
month[8]=31
month[9]=30
month[10]=31
month[11]=30
month[12]=31

midx=[0 for i in range(13)]
for i in range(2,13):
  midx[i]+=midx[i-1]+month[i-1]

l=[]
for i in range(N):
  a,b,c,d=map(int,input().split())
  if a>11 or c<3:
    continue
  l.append([a,b,c,d])
l.sort()

answer=0

[a,b,c,d]=l[0]
if midx[a]+b-1>midx[3]:
  print(0)
  exit(0)
start=deque([midx[a]+b-1])
end=deque([midx[c]+d-1])

startidx=len(l)
for i in range(1,len(l)):
  [a,b,c,d]=l[i]
  if a==3 and b==1:
    if end[0]<midx[c]+d-1:
      start=deque([midx[a]+b-1])
      end=deque([midx[c]+d-1])
    continue
  if a>=3:
    startidx=i
    break
  if end[0]<midx[c]+d-1:
    start=deque([midx[a]+b-1])
    end=deque([midx[c]+d-1])

if end[0]>=midx[12]:
  print(1)
  exit(0)

if startidx==len(l):
  print(0)
  exit(0)

for i in range(startidx,len(l)):
  [a,b,c,d]=l[i]
  s=midx[a]+b-1
  e=midx[c]+d-1
  while end:
    if end[0]<s:
      end.popleft()
      start.popleft()
      answer+=1
    else:
      break
  if not end:
    print(0)
    exit(0)
  if start[-1]==s:
    start.pop()
    end.pop()
    start.append(s)
    end.append(e)
    continue
  if end[-1]<e:
    if len(end)>=2:
      end.pop()
      start.pop()
    start.append(s)
    end.append(e)
    if e>=midx[12]:
      break

if end[-1]<midx[12]:
  print(0)
  exit(0)

answer+=len(start)
print(answer)
