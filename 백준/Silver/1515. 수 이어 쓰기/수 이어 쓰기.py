import sys
from collections import deque
input=sys.stdin.readline

n=deque(input().rstrip())

i=1
while True:
  now=list(str(i))
  for item in now:
    if item==n[0]:
      n.popleft()
      if not n:
        break
  if not n:
    print(i)
    break
  i+=1

