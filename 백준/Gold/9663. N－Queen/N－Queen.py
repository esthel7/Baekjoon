import sys
input=sys.stdin.readline

def find(idx):
  global answer
  if idx==N:
    answer+=1
    return

  non={}
  for i in range(idx):
    diff=idx-i
    non[dp[i]+diff]=True
    non[dp[i]-diff]=True

  for i in range(N):
    if remain[i] and i not in non:
      remain[i]=False
      dp[idx]=i
      find(idx+1)
      remain[i]=True

N=int(input())
dp=[-1 for i in range(N)]
remain=[True for i in range(N)]

answer=0
for i in range(N):
  dp[0]=i
  remain[i]=False
  find(1)
  remain[i]=True

print(answer)
