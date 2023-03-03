import sys
input = sys.stdin.readline

n,m=map(int,input().split())
v=list(map(int,input().split()))
cnt=[]
for i in range(n):
    if i!=0:
        cnt.insert(i,cnt[i-1]+v[i])
    else:
        cnt.insert(0,v[i])
for a in range(m):
    i,j=map(int,input().split())
    if i==1:
        print(cnt[j-1])
    else:
        print(cnt[j-1]-cnt[i-2])