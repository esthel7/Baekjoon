import sys
input=sys.stdin.readline

l=list(input().rstrip())

# 0 앞에는 반드시 1 or 2

L=len(l)
dp=[0 for i in range(L)]
if L==0:
  print(0)
  exit(0)

if l[0]<='0' or l[0]>'9':
  print(0)
  exit(0)
dp[0]=1

if L>=2:
  if l[1]<'0' or l[1]>'9':
    print(0)
    exit(0)

  now=0
  if l[1]!='0':
    now+=1
  if l[0]=='1' or (l[0]=='2' and l[1]<='6'):
    now+=1
  if now==0:
    print(0)
    exit(0)
  dp[1]=now

for i in range(2,L):
  now=0
  if l[i]<'0' or l[i]>'9':
    print(0)
    exit(0)

  if l[i]!='0':
    now+=dp[i-1]
  if l[i-1]=='1' or (l[i-1]=='2' and l[i]<='6'):
    now+=dp[i-2]
  if now==0:
    print(0)
    exit(0)
  dp[i]=now%1000000

print(dp[L-1])
