import sys
input=sys.stdin.readline

N,M=map(int,input().split())
e=[]
root=[0 for i in range(N+1)]
count=0
for i in range(M):
    a,b=map(int,input().split())
    if b<a:
        cnt=b
        b=a
        a=cnt

    if root[a]==0:
        if root[b]==0: # new new
            root[a]=a
            root[b]=a
            count+=1
        else: # new old
            root[a]=root[b]
    else:
        if root[b]==0: # old new
            root[b]=root[a]
        else: # old old
            if root[a]!=root[b]:
                B=root[b]
                count-=1
                for j in range(1,N+1):
                    if root[j]==B:
                        root[j]=root[a]

for i in range(1,N+1):
    if root[i]==0:
        count+=1
    
print(count)
