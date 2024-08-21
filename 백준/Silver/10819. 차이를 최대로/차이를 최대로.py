import sys
input=sys.stdin.readline

def calculate(now):
  global answer
  check=0
  for i in range(1,N):
    check+=abs(l[now[i-1]]-l[now[i]])
  answer=max(answer,check)

def make(now):
  if len(now)==N:
    calculate(now)
    return
  for i in range(N):
    if i in now:
      continue
    now.append(i)
    make(now)
    now.pop()

N=int(input())
l=list(map(int,input().split()))
answer=0
make([])
print(answer)
