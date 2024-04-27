import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline

def find(num):
  if num!=info[num]:
    info[num]=find(info[num])
  return info[num]

def change(A,B):
  a=find(A)
  b=find(B)
  if a>b:
    info[a]=b
  else:
    info[b]=a

n,m=map(int,input().split())

info=[i for i in range(n+1)] # group idx

for _ in range(m):
  flag,a,b=map(int,input().split())
  if flag==0:
    change(info[b],info[a])
    # print('after',info)
  else:
    if find(a)==find(b):
      print('yes')
    else:
      print('no')
