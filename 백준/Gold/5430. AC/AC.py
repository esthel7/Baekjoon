import sys
from collections import deque
input=sys.stdin.readline

def find(p,n,l):
  q=deque()
  for i in range(n):
    q.append(int(l[i]))
  
  flag=True # leftpop
  for i in range(len(p)):
    now=p[i]
    if now=='R':
      flag=not flag
    else:
      if not len(q):
        print('error')
        return
      if flag:
        a=q.popleft()
      else:
        a=q.pop()

  print('[',end='')
  if flag:
    if len(q):
      print('%d'%q[0],end='')
    for i in range(1,len(q)):
      print(',%d'%q[i],end='')
  else:
    if len(q):
      print('%d'%q[len(q)-1],end='')
    for i in range(len(q)-2,-1,-1):
      print(',%d'%q[i],end='')
  print(']')

T=int(input())
for i in range(T):
  p=list(input().rstrip())
  n=int(input())
  l=input().rstrip()
  l=l[1:len(l)-1]
  l=l.split(',')
  if l[0]=='':
    l=[]
  
  find(p,n,l)

