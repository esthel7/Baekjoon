import sys
input=sys.stdin.readline

T=int(input())
for _ in range(T):
  n,k,t,m=map(int,input().split())

  team=[[0 for i in range(k+1)] for i in range(n+1)]
  tries=[0 for i in range(n+1)]
  time=[0 for i in range(n+1)]

  for submit in range(m):
    i,j,s=map(int,input().split())
    team[i][j]=max(team[i][j],s)
    tries[i]+=1
    time[i]=submit

  answer=n
  team[t]=sum(team[t])
  for i in range(1,n+1):
    if i==t:
      continue
    team[i]=sum(team[i])
    if team[t]>team[i]:
      answer-=1
    elif team[t]<team[i]:
      continue
    else:
      if tries[t]<tries[i]:
        answer-=1
      elif tries[t]>tries[i]:
        continue
      else:
        if time[t]<time[i]:
          answer-=1

  print(answer)
