N=int(input())
l=[[0 for i in range(10)]for j in range(N+1)]
l[0][0]=1

for i in range(1,N+1):
  for j in range(10):
    if l[i-1][j]==0:
      break
    for k in range(j,10):
      l[i][k]+=l[i-1][j]

total=0
for i in range(10):
  total+=l[N][i]
print(total%10007)
