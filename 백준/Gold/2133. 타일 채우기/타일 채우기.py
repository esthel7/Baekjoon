import sys
input=sys.stdin.readline

# 2칸은 3개, 4칸뒤 2개, 6칸뒤 2개, 8칸뒤 2개 ...

N=int(input())
if N%2==1:
  print(0)
  exit(0)

if N==2:
  print(3)
  exit(0)

dp=[2 for i in range(N//2+1)]
dp[0]=0
dp[1]=3
dp[2]=11
total=[0 for i in range(N//2+1)]
total[1]=3
total[2]=14
for i in range(3,N//2+1):
  dp[i]+=dp[i-1]*3+total[i-2]*2 # 2칸마다 3개, 4,6,8마다 2개씩 추가
  total[i]+=dp[i]+total[i-1]

print(dp[N//2])
