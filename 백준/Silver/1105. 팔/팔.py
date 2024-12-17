import sys
input=sys.stdin.readline

L,R=input().rstrip().split()
L=list(L)
R=list(R)

if len(L)!=len(R):
  print(0)
  exit()

answer=0
for i in range(len(L)):
  if L[i]!=R[i]:
    print(answer)
    exit()
  if L[i]=='8':
    answer+=1

print(answer)
