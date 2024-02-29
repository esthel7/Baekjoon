import sys
from collections import deque
input=sys.stdin.readline

def find(n):
  dp[1]=1
  dp[2]=2
  dp[3]=4
  for i in range(4,n):
    dp[i]=(dp[i-1]+dp[i-2]+dp[i-3])%1000000009

T=int(input())
l=[]
for i in range(T):
  l.append(int(input()))

Max=max(l)+1
dp=[0 for i in range(Max)]
find(Max)
for now in l:
  print(dp[now])
