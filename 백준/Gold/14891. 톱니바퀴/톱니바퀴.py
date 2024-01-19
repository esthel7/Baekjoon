import sys
from collections import deque
input=sys.stdin.readline

# 극이 다르다면 회전한 방향과 반대로 회전
# N극 0, S극 1

def move(num,dir):
  if dir==1:
    left=l[num].pop()
    l[num].appendleft(left)
  else:
    left=l[num].popleft()
    l[num].append(left)

def find(num,dir):
  dirs=[0 for i in range(4)]
  dirs[num]=dir

  s=[[num,dir]]
  for i in range(num+1,4):
    right=l[i-1][2]
    dir=dirs[i-1]
    if l[i][6]!=right:
      if dir==1:
        s.append([i,-1])
        dirs[i]=-1
      else:
        s.append([i,1])
        dirs[i]=1
    else:
      break

  for i in range(num-1,-1,-1):
    left=l[i+1][6]
    dir=dirs[i+1]
    if l[i][2]!=left:
      if dir==1:
        s.append([i,-1])
        dirs[i]=-1
      else:
        s.append([i,1])
        dirs[i]=1
    else:
      break
  
  for [num,dir] in s:
    move(num,dir)


l=deque([])
for i in range(4):
  l.append(deque(input().rstrip()))

N=int(input())
for i in range(N):
  num,dir=map(int,input().split())
  find(num-1,dir)

total=0
if l[0][0]=='1':
  total+=1
if l[1][0]=='1':
  total+=2
if l[2][0]=='1':
  total+=4
if l[3][0]=='1':
  total+=8

print(total)
