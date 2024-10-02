import sys
input=sys.stdin.readline

N=int(input())
info={}
change={}
l=[]
for _ in range(N):
  now=list(input().rstrip())
  l.append(now)
  num=1
  for i in range(len(now)-1,-1,-1):
    if now[i] not in info:
      change[now[i]]=0
      info[now[i]]=0
    info[now[i]]+=num
    num*=10

s=[]
for key in info.keys():
  s.append([info[key],key])
s.sort(reverse=True)

num=9
for total,key in s:
  change[key]=num
  num-=1

total=0
for ll in l:
  now=0
  num=1
  for i in range(len(ll)-1,-1,-1):
    now+=change[ll[i]]*num
    num*=10
  total+=now

print(total)
