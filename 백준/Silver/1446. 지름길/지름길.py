import sys
input=sys.stdin.readline

N,D=map(int,input().split())
info={}
for i in range(N):
  start,end,dist=map(int,input().split())
  if end>D or dist>end-start:
    continue
  if start in info:
    if end in info[start]:
      if info[start][end]>dist:
        info[start][end]=dist
    else:
      info[start][end]=dist
  else:
    info[start]={end:dist}

dp=[D for i in range(D+1)]
dp[0]=0
if 0 in info:
  for key in info[0]:
    if dp[key]>info[0][key]:
      dp[key]=info[0][key]

for i in range(1,D+1):
  if dp[i]>dp[i-1]+1:
    dp[i]=dp[i-1]+1
  if i in info:
    for key in info[i]:
      if dp[key]>info[i][key]+dp[i]:
        dp[key]=info[i][key]+dp[i]
print(dp[D])