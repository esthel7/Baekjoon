import sys
input=sys.stdin.readline

N=int(input())
l=list(map(int,input().split()))

info={}
for i in range(N):
  for key in info.keys():
    value=(l[i]-l[key])/(i-key)
    if info[key][1]==0 or info[key][0]<value:
      info[key][0]=value
      info[key][1]+=1
  info[i]=[0,0]

rinfo={}
for i in range(N-1,-1,-1):
  for key in rinfo.keys():
    value=(l[i]-l[key])/(i-key)
    if rinfo[key][1]==0 or rinfo[key][0]>value:
      rinfo[key][0]=value
      rinfo[key][1]+=1
  rinfo[i]=[0,0]

answer=0
for i in range(N):
  now=info[i][1]+rinfo[i][1]
  if now>answer:
    answer=now

print(answer)
