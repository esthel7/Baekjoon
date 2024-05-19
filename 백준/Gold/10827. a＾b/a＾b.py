import sys
from collections import deque
input=sys.stdin.readline

a,b=input().rstrip().split()
a=list(a)
b=int(b)

for i in range(len(a)):
  if a[i]=='.':
    a.pop(i)
    left=len(a)-i
    break

a=int(''.join(a))

a=a**b
a=deque(str(a))
left*=b

A=len(a)
if A<=left:
  for i in range(left-A+1):
    a.appendleft('0')
    A+=1

a.insert(A-left,'.')
print(''.join(a))
