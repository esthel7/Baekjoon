import sys
input=sys.stdin.readline

T=int(input())
for _ in range(T):
  n=int(input())
  l=[0]+list(map(int,input().split()))

  team=0
  visited=[False for i in range(n+1)]

  for i in range(1,n+1):
    if visited[i]:
      continue

    visited[i]=True
    s=[i]
    now=i
    while True:
      if visited[l[now]]:
        cnt=0
        while s:
          item=s.pop()
          cnt+=1
          if item==l[now]:
            team+=cnt
            break
        break
      else:
        visited[l[now]]=True
        s.append(l[now])
        now=l[now]

  print(n-team)
