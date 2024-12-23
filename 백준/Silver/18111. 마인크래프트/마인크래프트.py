import sys
input=sys.stdin.readline

N,M,B=map(int,input().split())
info={}
Max=-1
Min=260
for i in range(N):
  now=list(map(int,input().split()))
  for j in range(M):
    if now[j]>Max:
      Max=now[j]
    if now[j]<Min:
      Min=now[j]
    if now[j] in info:
      info[now[j]]+=1
    else:
      info[now[j]]=1

answer=[-1,-1]
for i in range(Min,Max+1):
  have=B
  time=0
  for key in info.keys():
    if key<i:
      have-=(i-key)*info[key]
      time+=(i-key)*info[key]
    elif key>i:
      have+=(key-i)*info[key]
      time+=2*(key-i)*info[key]
  if have<0:
    break
  if answer[0]>time or answer[0]==-1:
    answer=[time,i]
  elif answer[0]==time:
    answer[1]=i

print(*answer)
