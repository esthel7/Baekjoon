import sys
from collections import deque
input=sys.stdin.readline

# 대문자, 소문자, 숫자, 백스페이스, 화살표

def find():
  left=deque([])
  right=deque([])
  for i in range(len(l)):
    if l[i]=='<':
      if left:
        right.appendleft(left.pop())
    elif l[i]=='>':
      if right:
        left.append(right.popleft())
    elif l[i]=='-':
      if left:
        left.pop()
    else:
      left.append(l[i])

  final=left+right
  return ''.join(final)


T=int(input())
for i in range(T):
  l=list(input().rstrip())
  print(find())

