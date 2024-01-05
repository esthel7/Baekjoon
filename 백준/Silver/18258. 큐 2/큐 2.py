import sys
from collections import deque
input=sys.stdin.readline

N=int(input())
s=deque()
for i in range(N):
  a=input().rstrip()
  b=a.split(' ')
  if len(b)==2:
    s.append(b[1])
    continue
  if a[0]=='p': # pop
    if len(s):
      print(s.popleft())
    else:
      print(-1)
    continue
  if a[0]=='s': # size
    print(len(s))
    continue
  if a[0]=='e': # empty
    if len(s):
      print(0)
    else:
      print(1)
    continue
  if a[0]=='f': # front
    if len(s):
      print(s[0])
    else:
      print(-1)
    continue
  if a[0]=='b': # back
    if len(s):
      print(s[-1])
    else:
      print(-1)
  continue
