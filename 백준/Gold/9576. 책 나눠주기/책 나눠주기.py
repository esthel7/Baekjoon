import sys
input=sys.stdin.readline

T=int(input())
for _ in range(T):
  N,M=map(int,input().split())

  dp=[[] for i in range(N+2)]
  for i in range(M):
    a,b=map(int,input().split())
    dp[a].append([i,b])
    dp[b+1].append([-i,0])

  answer=0
  now={}
  left={}

  for i in range(N+1):
    for idx,last in dp[i]:
      if last==0:
        if -idx in now:
          now.pop(-idx)
        continue
      now[idx]=last

    Min=2000
    num=-1
    for key in now.keys():
      if Min>now[key]:
        Min=now[key]
        num=key
    if num!=-1:
      left[num]=True
      now.pop(num)
      answer+=1

  print(answer)

