import sys
input=sys.stdin.readline

N=int(input())
l=[]
for i in range(N):
  l.append(int(input()))

save=[0 for i in range(N+1)]
save[l[0]]=1
for i in range(1,N):
  now=l[i]
  Max=0
  for j in range(now-1,0,-1):
    if Max<save[j]:
      Max=save[j] 
  save[now]=Max+1

print(N-max(save))

