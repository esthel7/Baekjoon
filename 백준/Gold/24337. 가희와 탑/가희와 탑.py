import sys
from collections import deque
input=sys.stdin.readline

N,a,b=map(int,input().split())

if a+b-1>N:
  print(-1)
  exit(0)

left=deque([])
right=deque([])

if a==1:
  for i in range(b,0,-1):
    right.append(i)
  first=right.popleft()
  for i in range(N-a-b+1):
    right.appendleft(1)
  right.appendleft(first)
else:
  if a+b-1==N:
    # 6 5 2 -> 123451
    # 6 6 1 -> 123456
    # 6 2 5 -> 154321
    # 6 1 6 -> 654321
    # 7 4 4 -> 1234321
    if a>=b:
      for i in range(1,a+1):
        left.append(i)
      for i in range(b-1,0,-1):
        right.append(i)
    else:
      for i in range(1,a):
        left.append(i)
      for i in range(b,0,-1):
        right.append(i)
  elif a+b==N:
    # 6 4 2 -> 123411
    # 6 2 4 -> 114321
    # 6 1 5 -> 554321
    # 6 3 3 -> 123321
    # 8 5 3 -> 12345121
    # 10 6 4 -> 1234561321
    if a>=b:
      for i in range(1,a+1):
        left.append(i)
      for i in range(b-1,0,-1):
        right.append(i)
      right.appendleft(1)
    else:
      for i in range(1,a):
        left.append(i)
      for i in range(b,0,-1):
        right.append(i)
  else:
    # 6 1 1 -> 111111
    # 6 2 1 -> 121112
    # 6 1 2 -> 211121
    # 6 2 3 -> 111321
    # 6 3 2 -> 111231
    if a>=b:
      for i in range(1,a+1):
        left.append(i)
      for i in range(b-1,0,-1):
        right.append(i)
      for i in range(N-a-b+1):
        left.appendleft(1)
    else:
      for i in range(1,a):
        left.append(i)
      for i in range(b,0,-1):
        right.append(i)
      for i in range(N-a-b+1):
        left.appendleft(1)

for i in left:
  print(i,end=' ')
for i in right:
  print(i,end=' ')
print()

