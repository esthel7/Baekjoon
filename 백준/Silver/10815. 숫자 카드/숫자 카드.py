import sys
input=sys.stdin.readline

N=int(input())
have=list(map(int,input().split()))
have.sort()

M=int(input())
l=list(map(int,input().split()))

for i in range(M):
  start=0
  end=N-1
  printflag=False
  while start<=end:
    mid=(start+end)//2
    if have[mid]==l[i]:
      print(1,end=' ')
      printflag=True
      break
    if have[mid]<l[i]:
      start=mid+1
    else:
      end=mid-1
  if not printflag:
    print(0,end=' ')

print()
