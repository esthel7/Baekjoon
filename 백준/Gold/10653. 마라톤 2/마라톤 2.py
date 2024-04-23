import sys
input=sys.stdin.readline

# N개의 체크포인트, 중간 K개 건너뛰기
# 1,N은 유지

N,K=map(int,input().split())
l=[[0,0]]
for i in range(N):
  l.append(list(map(int,input().split())))

diff=[[0 for i in range(N+1)]for j in range(N+1)]
for i in range(1,N+1):
  for j in range(i+1,i+K+2):
    if j>N:
      break
    value=abs(l[i][0]-l[j][0])+abs(l[i][1]-l[j][1])
    diff[i][j]=value
    diff[j][i]=value

last=10000000
answer=last
point=[[last for i in range(K+1)]for j in range(N+1)]
point[1][0]=0

for i in range(1,N+1):
  for j in range(K+1):
    if point[i][j]==last or point[i][j]>answer:
      continue
    for k in range(j,K+1):
      if i+1+k-j>N:
        break
      point[i+1+k-j][k]=min(point[i+1+k-j][k],point[i][j]+diff[i][i+1+k-j])
      if i+1+k-j==N:
        answer=min(answer,point[i+1+k-j][k])

print(answer)
