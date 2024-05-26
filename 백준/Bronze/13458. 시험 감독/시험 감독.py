import sys
input=sys.stdin.readline

N=int(input())
l=list(map(int,input().split()))
B,C=map(int,input().split())

# 총감독관은 B명 감당, 부감독관은 C명 감당
# 총감독관 1명 ,부감독 여러명

cnt=0
for i in range(len(l)):
  if l[i]<=B:
    cnt+=1
    continue
  cnt+=1
  l[i]-=B
  if l[i]%C==0:
    cnt+=l[i]//C
  else:
    cnt+=l[i]//C+1

print(cnt)
