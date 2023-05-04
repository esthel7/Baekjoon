import sys
input=sys.stdin.readline

N=int(input())

i=0
j=0
count=0
now=0
while j<=N:
    if now>N:
        now-=i
        i+=1
    elif now<N:
        j+=1
        now+=j
    else:
        # print('append',i,j)
        count+=1
        now-=i
        i+=1
        j+=1
        now+=j

print(count)
