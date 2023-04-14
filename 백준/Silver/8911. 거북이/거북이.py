import sys
input=sys.stdin.readline

def find(start):
    now=[0,0] # 세로, 가로
    max1=0
    max2=0
    min1=0
    min2=0
    f=[0,1] # 0번째가 1
    for i in range(len(l[start])):
        change,move=f
        if l[start][i]=='F':
            now[change]+=move
            if change==0:
                if now[change]>max1:
                    max1=now[change]
                if now[change]<min1:
                    min1=now[change]
            if change==1:
                if now[change]>max2:
                    max2=now[change]
                if now[change]<min2:
                    min2=now[change]
        elif l[start][i]=='B':
            now[change]-=move
            if change==0:
                if now[change]>max1:
                    max1=now[change]
                if now[change]<min1:
                    min1=now[change]
            if change==1:
                if now[change]>max2:
                    max2=now[change]
                if now[change]<min2:
                    min2=now[change]
        elif l[start][i]=='L':
            if f==[0,1]:
                f=[1,-1]
            elif f==[0,-1]:
                f=[1,1]
            elif f==[1,1]:
                f=[0,1]
            elif f==[1,-1]:
                f=[0,-1]
        elif l[start][i]=='R':
            if f==[0,1]:
                f=[1,1]
            elif f==[0,-1]:
                f=[1,-1]
            elif f==[1,1]:
                f=[0,-1]
            elif f==[1,-1]:
                f=[0,1]
    
    if max1==min1 or max2==min2:
        return 0
    return (max1-min1)*(max2-min2)


T=int(input())
l=[]
for i in range(T):
    l.append(list(input().rstrip()))

for i in range(T):
    print(find(i))
