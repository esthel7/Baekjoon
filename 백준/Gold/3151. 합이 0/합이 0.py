import sys
from collections import deque
input=sys.stdin.readline

N=int(input())
l=list(map(int,input().split()))
l.sort()

def notVisit(left,right):
  if left not in visited:
    visited[left]={right:True}
    return True
  if right not in visited[left]:
    visited[left][right]=True
    return True
  return False

answer=0
for i in range(N-2):
  now=l[i]
  left=i+1
  right=N-1
  while left<right:
    value=l[left]+l[right]
    if now+value==0:
      if l[left]==l[right]:
        diff=right-left+1
        answer+=diff*(diff-1)//2
        break
      mleft=left
      while mleft<right:
        if mleft+1<right and l[mleft]==l[mleft+1]:
          mleft+=1
        else:
          break
      mright=right
      while left<mright:
        if left<mright-1 and l[mright]==l[mright-1]:
          mright-=1
        else:
          break
      if mleft==left:
        if mright==right:
          answer+=1
          left+=1
          continue
        answer+=right-mright+1
        right=mright-1
      else:
        if mright==right:
          answer+=mleft-left+1
          left=mleft+1
          continue
        answer+=(mleft-left+1)*(right-mright+1)
        left=mleft+1
        right=mright-1
    elif now+value>0:
      right-=1
    else:
      left+=1

print(answer)
