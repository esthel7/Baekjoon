import sys
input=sys.stdin.readline

N=int(input())
info={}
Max=0
num=-1
for i in range(N):
    now=int(input())
    if now in info:
        info[now]+=1
        if Max<info[now]:
            Max=info[now]
            num=now
        elif Max==info[now] and num>now:
            num=now
    else:
        info[now]=1
        if Max<info[now]:
            Max=info[now]
            num=now
        elif Max==info[now] and num>now:
            num=now
print(num)