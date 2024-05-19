import sys
input=sys.stdin.readline

def find(now,B):
  if B==1:
    return now

  if B%2==1:
    return (now*find(now,B-1))%num
  Find=find(now,B//2)
  return (Find*Find)%num


A,B=map(int,input().split())
num=1000000007
if A==1:
  print(B%num)
  exit(0)
if B==1:
  print(1)
  exit(0)

AB=find(A,B) # A^B
if AB==0:
  AB=num
ANUM=find(A-1,num-2) # (A-1)^(num-2)
print(((AB-1)*ANUM)%num)
