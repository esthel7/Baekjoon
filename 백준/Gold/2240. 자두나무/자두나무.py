import sys
input=sys.stdin.readline

# 최대 w번 움직이기

def make(T):
  if l[0]==2:
    num.append(0)
  numbers=1
  for i in range(1,T):
    if l[i-1]!=l[i]:
      num.append(numbers)
      numbers=0
    numbers+=1
  num.append(numbers)


def find(T,W,start,pickNum,startNum):
  if final[pickNum][start]<startNum+num[start]:
    final[pickNum][start]=startNum+num[start]
  else:
    return

  for i in range(start+2,T,2):
    if pickNum+1<=W:
      find(T,W,i-1,pickNum+1,final[pickNum][i-2])
    if final[pickNum][i]<final[pickNum][i-2]+num[i]:
      final[pickNum][i]=final[pickNum][i-2]+num[i]
    else:
      break

  if T>=2:
    Max=max(final[pickNum][T-2],final[pickNum][T-1])
  else:
    Max=final[pickNum][T-1]
  if answer[0]<Max:
    answer[0]=Max

  if T+1%2!=start%2 and T-2>=0 and pickNum+1<=W:
    find(T,W,T-1,pickNum+1,final[pickNum][T-2])


T,W=map(int,input().split())
l=[]
for i in range(T):
  l.append(int(input()))

num=[]
make(T)
T=len(num)

final=[[0 for i in range(T)]for j in range(W+1)]
final[0][0]=-1

answer=[0]
find(T,W,0,0,0)
print(answer[0])
