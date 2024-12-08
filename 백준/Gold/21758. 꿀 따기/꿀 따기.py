import sys
input=sys.stdin.readline

N=int(input())
l=list(map(int,input().split()))

total=[0 for i in range(N)]
total[0]=l[0]
for i in range(1,N):
  total[i]=total[i-1]+l[i]

answer=0
for i in range(1,N-1):
  right=total[N-1]*2-total[i]-l[i]-l[0]
  left=total[N-1]-l[N-1]+total[i]-l[i]*2
  mid=total[i]-l[0]+total[N-1]-total[i-1]-l[N-1]
  answer=max(answer,right,left,mid)

print(answer)
