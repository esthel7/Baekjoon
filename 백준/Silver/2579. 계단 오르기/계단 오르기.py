import sys
input=sys.stdin.readline

# 연속 세계단 불가
# 마지막 밟기

n=int(input())
l=[0,0]
for i in range(n):
  l.append(int(input()))
n+=2

num=[[0,0] for i in range(n)]
for i in range(2,n):
  num[i][0]=num[i-1][1]+l[i] # 건너뛰기 후 전 밟기
  num[i][1]=max(num[i-2])+l[i]

print(max(num[n-1]))
