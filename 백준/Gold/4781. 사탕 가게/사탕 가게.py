import sys
input=sys.stdin.readline

while True:
  n,m=map(float,input().split())
  n=int(n)
  m=int(m*100+0.5)
  if n==0 and m==0:
    break

  last=m+1
  dp=[0 for i in range(last)]

  for i in range(n):
    c,p=map(float,input().split())
    c=int(c)
    p=int(p*100+0.5)

    for j in range(p,last):
      if dp[j-p]+c>dp[j]:
        dp[j]=dp[j-p]+c
      if dp[j-1]>dp[j]:
        dp[j]=dp[j-1]

  print(dp[last-1])
