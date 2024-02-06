def check(num):
  if num>0:
    return True
  return False

N=int(input())
now=list(map(int,input().split()))
right=list(map(int,input().split()))

diff=[]
for i in range(N):
  diff.append(right[i]-now[i])

dp=[0 for i in range(N)]
prev=0
for i in range(N):
  if diff[i]==0:
    dp[i]=dp[i-1]
    prev=0
    continue

  if prev==0:
    dp[i]=dp[i-1]+abs(diff[i])
    prev=diff[i]
  else:
    prevFlag=check(prev)
    if prevFlag==check(diff[i]):
      if prevFlag: # 양수
        if prev<diff[i]:
          dp[i]=dp[i-1]+diff[i]-prev
        else:
          dp[i]=dp[i-1]
      else: # 음수
        if prev>diff[i]:
          dp[i]=dp[i-1]+prev-diff[i]
        else:
          dp[i]=dp[i-1]
    else:
      dp[i]=dp[i-1]+abs(diff[i])
    prev=diff[i]

print(dp[N-1])
