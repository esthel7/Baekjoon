import sys
input=sys.stdin.readline

# M과 N보다 작거나 같은 두 개의 자연수로 년도를 표시

def find(M,N,x,y):
  breakFlag=False
  if x==y==0:
    start=M
  else:
    start=x

  for i in range(start,M*N+1,M):
    if i%M==x and i%N==y:
      print(i)
      breakFlag=True
      break
  if not breakFlag:
    print(-1)

T=int(input())
for i in range(T):
  M,N,x,y=map(int,input().split())
  if x==M:
    x=0
  if y==N:
    y=0
  find(M,N,x,y)
