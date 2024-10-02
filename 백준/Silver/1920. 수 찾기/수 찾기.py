import sys
input=sys.stdin.readline

def check(num):
  if num in info:
    return 1
  return 0

N=int(input())
A=list(map(int,input().split()))
M=int(input())
B=list(map(int,input().split()))

info={}
for i in range(N):
  info[A[i]]=True

for i in range(M):
  print(check(B[i]))
