import sys
input=sys.stdin.readline

def find(now,start):
  if len(now)==M:
    for i in range(M):
      print(now[i],end=' ')
    print()
    return
  for i in range(start,N+1):
    now.append(i)
    find(now,i+1)
    now.pop()

N,M=map(int,input().split())
find([],1)
