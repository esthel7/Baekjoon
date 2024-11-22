import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def change(x,y):
  for i in range(x,x+3):
    for j in range(y,y+3):
      if A[i][j]=='0':
        A[i][j]='1'
      else:
        A[i][j]='0'

def find(x,y,cnt):
  global answer
  for i in range(x,N):
    for j in range(M):
      if A[i][j]!=B[i][j]:
        if i+3<=N and j+3<=M:
          change(i,j)
          find(i,j,cnt+1)
          return
        else:
          return
  if answer==-1 or answer>cnt:
    answer=cnt


N,M=map(int,input().split())
A=[]
for i in range(N):
  A.append(list(input().rstrip()))
B=[]
for i in range(N):
  B.append(list(input().rstrip()))

answer=-1
find(0,0,0)
print(answer)
