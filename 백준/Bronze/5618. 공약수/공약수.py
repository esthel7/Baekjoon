import sys
from collections import deque
input=sys.stdin.readline

def find(idx,flag):
  global possible
  left=deque([])
  right=[]
  for i in range(1,int(idx**(0.5))+1):
    if idx%i==0:
      left.appendleft(i)
      if i!=idx//i:
        right.append(idx//i)

  if flag:
    possible=deque([])
    possible+=right
    possible+=left
    return

  if not possible:
    possible+=right
    possible+=left
  else:
    now=[]
    now+=right
    now+=left
    while True:
      if possible[0] in now:
        find(possible[0],True)
        break
      possible.popleft()



n=int(input())
l=list(map(int,input().split()))
possible=deque([])

for i in range(n):
  find(l[i],False)

find(possible[0],True)

for i in range(len(possible)-1,-1,-1):
  print(possible[i])
