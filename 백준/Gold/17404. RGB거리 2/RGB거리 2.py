import sys
input=sys.stdin.readline

N=int(input())
l=[]
for i in range(N):
  l.append(list(map(int,input().split())))

def update(idx,color):
  # dp[idx][color][0]=min(dp[idx-1][color//][0])
  for i in range(3): # dp[idx][color][i]
    have=[]
    for j in range(3):
      if j==color or dp[idx-1][j][i]==0:
        continue
      have.append(dp[idx-1][j][i])
    if have:
      dp[idx][color][i]=min(have)+l[idx][color]

dp=[[[0,0,0] for i in range(3)]for j in range(N)]
dp[0][0]=[l[0][0],0,0]
dp[0][1]=[0,l[0][1],0]
dp[0][2]=[0,0,l[0][2]]

for i in range(1,N):
  for j in range(3):
    update(i,j)

answer=0
for i in range(3):
  for j in range(3):
    if i==j:
      continue
    if answer==0 or answer>dp[N-1][i][j]:
      answer=dp[N-1][i][j]

print(answer)
