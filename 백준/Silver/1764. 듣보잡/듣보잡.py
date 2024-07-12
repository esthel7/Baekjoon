import sys
input=sys.stdin.readline

N,M=map(int,input().split())
listen={}
for i in range(N):
  name=input().rstrip()
  listen[name]=True

answer=[]
for i in range(N):
  name=input().rstrip()
  if name in listen:
    answer.append(name)

print(len(answer))
answer.sort()
for key in answer:
  print(key)
