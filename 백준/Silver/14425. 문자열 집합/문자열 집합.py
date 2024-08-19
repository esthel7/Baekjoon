import sys
input=sys.stdin.readline

N,M=map(int,input().split())
info={}
for i in range(N):
  now=input().rstrip()
  info[now]=True

answer=0
for i in range(M):
  now=input().rstrip()
  if now in info:
    answer+=1
print(answer)
