import sys
input=sys.stdin.readline

N=int(input())

count=0
total=0
Min=1
for i in range(1,N+1):
    if total<N:
        total+=i
        while total>=N:
            if total==N:
                count+=1
            total-=Min
            Min+=1

print(count)
