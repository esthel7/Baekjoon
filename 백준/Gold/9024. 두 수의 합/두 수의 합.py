import sys
input=sys.stdin.readline

t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    num=list(map(int,input().split()))
    num.sort()

    mini=200000000
    for j in range(n):
        l=j+1
        r= n-1
        while(l<=r):
            mid=(l+r)//2
            s=num[j]+num[mid]
            if(s>k):
                r=mid-1
            else:
                l=mid+1
            if(abs(k-s)<mini):
                cnt=1
                mini=abs(k-s)
            elif(abs(k-s)==mini):
                cnt+=1
    print(cnt)