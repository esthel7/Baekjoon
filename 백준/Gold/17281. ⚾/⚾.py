import sys
from collections import deque
input=sys.stdin.readline

def calculate(now):
  now=deque(now)
  now.insert(3,0)

  value=0

  for num in range(N):
    p1=0
    p2=0
    p3=0
    out=0

    while out!=3:
      idx=now.popleft()
      now.append(idx)
      if l[num][idx]==0:
        out+=1
      elif l[num][idx]==4:
        value+=1
        value+=p1+p2+p3
        p1=0
        p2=0
        p3=0
      elif l[num][idx]==1:
        value+=p3
        p3=p2
        p2=p1
        p1=1
      elif l[num][idx]==2:
        value+=p3+p2
        p3=p1
        p2=1
        p1=0
      else: # 3
        value+=p3+p2+p1
        p3=1
        p2=0
        p1=0
  return value


def find(now):
  global answer
  if len(now)==8:
    value=calculate(now)
    if answer<value:
      answer=value
    return

  for i in range(1,9):
    if i in now:
      continue
    now.append(i)
    find(now)
    now.pop()


N=int(input())
l=[]
for i in range(N):
  l.append(list(map(int,input().split())))

answer=0
find(deque([]))
print(answer)
