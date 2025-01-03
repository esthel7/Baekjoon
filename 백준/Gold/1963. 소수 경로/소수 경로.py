import sys
from collections import deque
input=sys.stdin.readline

info=[True for i in range(10000)]
info[0]=False
info[1]=False
final={}
for i in range(2,10000):
  if info[i]:
    if i>=1000:
      final[str(i)]=True
    for j in range(i*2,10000,i):
      info[j]=False

def diff(a):
  for i in range(4):
    if a[i]!=B[i]:
      return True
  return False

T=int(input())
for _ in range(T):
  A,B=input().rstrip().split()
  A=list(A)
  B=list(B)

  first=''.join(A)
  visited={first:True}
  q=deque([[A,0]])
  flag=False
  while q:
    a,cnt=q.popleft()
    if not diff(a):
      print(cnt)
      flag=True
      break
    ca=list(a)
    for i in range(4):
      for j in range(10):
        ca[i]=str(j)
        check=''.join(ca)
        if check not in visited and check in final:
          visited[check]=True
          q.append([list(ca),cnt+1])
        ca[i]=a[i]

  if not flag:
    print('impossible')
