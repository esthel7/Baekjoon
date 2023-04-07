import sys
input=sys.stdin.readline

def find():
    if len(s)==M:
        for i in s:
            print(i,end=' ')
        print()
        return

    if len(s)==0:
        for i in range(N):
            s.append(i+1)
            find()
            s.pop()
    else:
        for i in range(s[-1]-1,N):
            s.append(i+1)
            find()
            s.pop()

N,M=map(int,input().split())

s=[]
find()
