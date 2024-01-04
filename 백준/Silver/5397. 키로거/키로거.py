import sys
from collections import deque
input=sys.stdin.readline

def make(l):
  before=deque()
  after=deque()

  for i in range(len(l)):
    if l[i]=='-':
      if len(before):
        before.pop()
    elif l[i]=='<':
      if len(before):
        a=before.pop()
        after.appendleft(a)
    elif l[i]=='>':
      if len(after):
        a=after.popleft()
        before.append(a)
    else:
      before.append(l[i])

  return ''.join(before)+''.join(after)

n=int(input())
l=[]
for i in range(n):
  l.append(list(input().rstrip()))
  print(make(l[i]))
