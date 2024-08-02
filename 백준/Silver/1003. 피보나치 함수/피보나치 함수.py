import sys
input=sys.stdin.readline

T=int(input())
dp0=[0 for i in range(41)]
dp1=[0 for i in range(41)]
dp0[0]=1
dp1[1]=1
for i in range(2,41):
  dp0[i]=dp0[i-1]+dp0[i-2]
  dp1[i]=dp1[i-1]+dp1[i-2]

for i in range(T):
  a=int(input())
  print(dp0[a],dp1[a])
