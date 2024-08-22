import sys
from collections import deque
input=sys.stdin.readline

left=deque(input().rstrip())
right=deque([])
N=int(input())
for i in range(N):
  enter=input().rstrip()
  if enter[0]=='P':
    enter=enter.split()
    left.append(enter[1])
    continue
  if enter=='D':
    if not len(right):
      continue
    left.append(right.popleft())
  elif enter=='L':
    if not len(left):
      continue
    right.appendleft(left.pop())
  else:
    if not len(left):
      continue
    left.pop()

print(''.join(left)+''.join(right))
