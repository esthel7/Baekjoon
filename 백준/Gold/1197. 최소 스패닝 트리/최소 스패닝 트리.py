import sys
input=sys.stdin.readline

# 가중치합 최소

def find():
    count=0
    while len(l):
        C,A,B=l.pop()
        if root[A]==0:
            count+=C
            if root[B]==0:
                root[A]=A
                root[B]=A
            else:
                root[A]=root[B]
        else:
            if root[A]!=root[B]:
                count+=C
                prev=root[B]
                root[B]=root[A]
                if prev!=0:
                    for i in range(1,V+1):
                        if root[i]==prev:
                            root[i]=root[A]
            else: # cycle
                continue
    print(count)

V,E=map(int,input().split())
l=[]
for i in range(E):
    A,B,C=map(int,input().split())
    if A<B:
        l.append([C,A,B])
    else:
        l.append([C,B,A])
l=sorted(l,reverse=True)
root=[0 for i in range(V+1)]
find()
