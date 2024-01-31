N=int(input())
pay=[0]+list(map(int,input().split()))
l=[-1 for i in range(N+1)]

for i in range(1,N+1):
  l[i]=pay[i]
  for j in range(1,i):
    l[i]=max(l[i],l[j]+pay[i-j])
print(l[N])
