import sys
input=sys.stdin.readline

# 0은 5,3,5, 1은 5, ... 이렇게 세로로 접근
def find():
    global check
    if num[0]==1:
        return 7
    if num[0]==3:
        if num[1]==1:
            return 4
        return 3
    if num[0]==4:
        if num[2]==5:
            return 9
        if check==0:
            return 2
        return 5
    if num[1]==2:
        return 0
    if num[2]==4:
        return 6
    return 8

N=int(input())
first=list(input().rstrip())

l=[]
for i in range(5):
    l.append(first[i*(N//5):(i+1)*(N//5)])
    # print(l[i])

final=[]
num=[]
check=0
for i in range(N//5):
    count=0
    for j in range(5):
        if l[j][i]=='#':
            count+=1
    if count==0: # 공백
        if len(num)==1:
            final.append(1)
        elif len(num)!=0:
            final.append(find())

        check=0
        num=[]
        continue
    if count==4: # 2, 5 구분
        if l[1][i]=='.':
            check=1 # 5
    else:
        check=0
    num.append(count)

if len(num):
    if len(num)==1:
        final.append(1)
    else:
        final.append(find())

for i in range(len(final)):
    print(final[i],end='')
