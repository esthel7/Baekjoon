import sys
from collections import deque
input=sys.stdin.readline

N=int(input())
for i in range(1,N+1):
  a,b,c=input().rstrip().split()
  a=list(a)
  b=list(b)
  c=list(c)

  A=len(a)
  B=len(b)
  C=len(c)

  check=deque([{}for i in range(2)])
  check[0]={0:{0:True}}
  for j in range(C):
    for ai in check[0].keys():
      for bi in check[0][ai].keys():
        if ai<A and c[j]==a[ai]:
          if ai+1 in check[1]:
            check[1][ai+1][bi]=True
          else:
            check[1][ai+1]={bi:True}
        if bi<B and c[j]==b[bi]:
          if ai in check[1]:
            check[1][ai][bi+1]=True
          else:
            check[1][ai]={bi+1:True}
    check.popleft()
    check.append({})

  answer='no'
  if A in check[0] and B in check[0][A]:
    answer='yes'

  print('Data set %d: %s'%(i,answer))
