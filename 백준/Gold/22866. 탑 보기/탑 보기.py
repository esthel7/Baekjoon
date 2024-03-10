import sys
input=sys.stdin.readline

N=int(input())
l=[0]+list(map(int,input().split()))

left=[0 for i in range(N+1)]
right=[0 for i in range(N+1)]
leftidx=[0 for i in range(N+1)]
rightidx=[0 for i in range(N+1)]

save=[[l[1],1]]
for i in range(2,N+1):
  if save[-1][0]<=l[i]:
    value,idx=save.pop()
    while save:
      if save[-1][0]<=l[i]:
        save.pop()
      else:
        break
  if save:
    left[i]=len(save)
    leftidx[i]=save[-1][1]
  save.append([l[i],i])

save=[[l[N],N]]
for i in range(N-1,0,-1):
  if save[-1][0]<=l[i]:
    value,idx=save.pop()
    while save:
      if save[-1][0]<=l[i]:
        save.pop()
      else:
        break
  if save:
    right[i]=len(save)
    rightidx[i]=save[-1][1]
  save.append([l[i],i])

for i in range(1,N+1):
  Len=left[i]+right[i]
  if Len==0:
    print(0)
    continue
  if leftidx[i]==0:
    print(Len,rightidx[i])
  elif rightidx[i]==0:
    print(Len,leftidx[i])
  else:
    if i-leftidx[i]<=rightidx[i]-i:
      print(Len,leftidx[i])
    else:
      print(Len,rightidx[i])

