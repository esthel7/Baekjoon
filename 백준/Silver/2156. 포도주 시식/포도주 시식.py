import sys
input=sys.stdin.readline

# 연속 3잔 불가

n=int(input())
l=[0,0,0]
for i in range(n):
  l.append(int(input()))

num=[[0,0,0] for i in range(n+3)]

for i in range(3,n+3):
  num[i][0]=max(num[i-3])+l[i] # 가장 큰 전전전값 더하기
  num[i][1]=max(num[i-2])+l[i] # 가장 큰 전전값 더하기
  num[i][2]=max(num[i-1][0],num[i-1][1])+l[i] # 전전값이 빠진 전값 더하기

print(max(max(num[n]),max(num[n+1]),max(num[n+2])))
