import sys
input=sys.stdin.readline

want=int(input())
a,b=map(int,input().split())
A=[]
for i in range(a):
  A.append(int(input()))
B=[]
for i in range(b):
  B.append(int(input()))

totalA=[A[0]]
for i in range(1,a*2-1):
  totalA.append(totalA[-1]+A[i%a])

infoA={totalA[a-1]:1}
totalA=[0]+totalA
for i in range(1,a+1):
  for j in range(i,i+a-1):
    now=totalA[j]-totalA[i-1]
    if now>want:
      continue
    if now in infoA:
      infoA[now]+=1
    else:
      infoA[now]=1

totalB=[B[0]]
for i in range(1,b*2-1):
  totalB.append(totalB[-1]+B[i%b])

infoB={totalB[b-1]:1}
totalB=[0]+totalB
for i in range(1,b+1):
  for j in range(i,i+b-1):
    now=totalB[j]-totalB[i-1]
    if now>want:
      continue
    if now in infoB:
      infoB[now]+=1
    else:
      infoB[now]=1

answer=0
if want in infoA:
  answer+=infoA[want]
if want in infoB:
  answer+=infoB[want]

for Akey in infoA.keys():
  left=want-Akey
  if left in infoB:
    answer+=infoA[Akey]*infoB[left]

print(answer)
