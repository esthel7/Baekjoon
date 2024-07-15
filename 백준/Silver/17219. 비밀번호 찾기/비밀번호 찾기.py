import sys
input=sys.stdin.readline

N,M=map(int,input().split())
info={}
for i in range(N):
  address,pw=input().rstrip().split(' ')
  info[address]=pw

for i in range(M):
  address=input().rstrip()
  print(info[address])

