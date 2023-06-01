import sys
input=sys.stdin.readline

def find():
    for i in range(N):
        for j in range(N):
            if r[i][j]==0 or l[i][j]==0:
                continue
            val=l[i][j]
            # right
            if j+val<N:
                r[i][j+val]+=r[i][j]
            # bottom
            if i+val<N:
                r[i+val][j]+=r[i][j]
    print(r[N-1][N-1])

N=int(input())
l=[]
r=[[0 for i in range(N)]for i in range(N)]
r[0][0]=1
for i in range(N):
    l.append(list(map(int,input().split())))

find()
