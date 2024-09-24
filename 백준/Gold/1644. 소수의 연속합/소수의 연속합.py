import sys
input=sys.stdin.readline

N=int(input())
if N<4:
  if N==2 or N==3:
    print(1)
  else:
    print(0)
  exit(0)

dp=[True for i in range(N+1)]
dp[0]=False
dp[1]=False
possible=[]
for i in range(2,N+1):
  if dp[i]:
    possible.append(i)
    for j in range(2*i,N+1,i):
      dp[j]=False

answer=0
start=0
end=1
now=possible[0]
Possible=len(possible)
while start<Possible:
  if now==N:
    # print('check',possible[start],possible[end])
    answer+=1
    now-=possible[start]
    start+=1
  elif now<N:
    if end+1<Possible:
      now+=possible[end]
      end+=1
    else:
      if possible[-1]==N:
        answer+=1
        # print('last')
      break
  else:
    now-=possible[start]
    start+=1

print(answer)
