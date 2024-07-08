import sys
from collections import deque
input=sys.stdin.readline

S=deque(input().rstrip())
T=deque(input().rstrip())
L=len(S)

while len(T)!=L:
  if T[-1]=='A':
    T.pop()
  else:
    T.pop()
    T.reverse()

if T==S:
  print(1)
else:
  print(0)
