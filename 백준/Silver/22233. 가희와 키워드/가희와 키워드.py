import sys
input=sys.stdin.readline

N,M=map(int,input().split())

info={}
for i in range(N):
  now=input().rstrip()
  info[now]=True

for i in range(M):
  words=input().rstrip().split(',')
  for word in words:
    if word in info:
      info.pop(word)

  print(len(info.keys()))
