import sys
input=sys.stdin.readline

T=int(input())
for _ in range(T):
  n=int(input())
  info={}
  for i in range(n):
    name,group=input().rstrip().split()
    if group in info:
      info[group].append(name)
    else:
      info[group]=[name]

  cnt=1
  for group in info.keys():
    cnt*=(len(info[group])+1)
  cnt-=1
  print(cnt)
