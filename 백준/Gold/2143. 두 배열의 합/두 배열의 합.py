import sys
input=sys.stdin.readline

def find():
  global answer
  for key in infoA.keys():
    left=T-key
    if left in infoB:
      answer+=infoA[key]*infoB[left]


T=int(input())
n=int(input())
A=list(map(int,input().split()))
infoA={}
for i in range(n):
  now=0
  for j in range(i,n):
    now+=A[j]
    if now in infoA:
      infoA[now]+=1
    else:
      infoA[now]=1

m=int(input())
B=list(map(int,input().split()))
infoB={}
for i in range(m):
  now=0
  for j in range(i,m):
    now+=B[j]
    if now in infoB:
      infoB[now]+=1
    else:
      infoB[now]=1

answer=0
find()
print(answer)
