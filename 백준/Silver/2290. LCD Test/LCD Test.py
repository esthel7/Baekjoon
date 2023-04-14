import sys
input=sys.stdin.readline

s,n=input().split() # 문자열 포함되어 있으므로 문자열로 입력받기
s=int(s)
n=list(n)

l=[[]for i in range(2*s+3)]

allSpace=' '*(s+2)
horizon=' '+'-'*s+' '
leftVertical='|'+' '*(s+1)
rightVertical=' '*(s+1)+'|'
halfVertical='|'+' '*s+'|'

for i in range(len(n)):
    if n[i]=='1':
        for j in range(2*s+3):
            if j==0 or j==s+1 or j==2*s+2:
                l[j].append(allSpace)
            else:
                l[j].append(rightVertical)
    elif n[i]=='2':
        for j in range(2*s+3):
            if j==0 or j==s+1 or j==2*s+2:
                l[j].append(horizon)
            elif j<s+1:
                l[j].append(rightVertical)
            else:
                l[j].append(leftVertical)
    elif n[i]=='3':
        for j in range(2*s+3):
            if j==0 or j==s+1 or j==2*s+2:
                l[j].append(horizon)
            else:
                l[j].append(rightVertical)
    elif n[i]=='4':
        for j in range(2*s+3):
            if j==0 or j==2*s+2:
                l[j].append(allSpace)
            elif j==s+1:
                l[j].append(horizon)
            elif j<s+1:
                l[j].append(halfVertical)
            else:
                l[j].append(rightVertical)
    elif n[i]=='5':
        for j in range(2*s+3):
            if j==0 or j==s+1 or j==2*s+2:
                l[j].append(horizon)
            elif j<s+1:
                l[j].append(leftVertical)
            else:
                l[j].append(rightVertical)
    elif n[i]=='6':
        for j in range(2*s+3):
            if j==0 or j==s+1 or j==2*s+2:
                l[j].append(horizon)
            elif j<s+1:
                l[j].append(leftVertical)
            else:
                l[j].append(halfVertical)
    elif n[i]=='7':
        l[0].append(horizon)
        for j in range(1,2*s+3):
            if j==s+1 or j==2*s+2:
                l[j].append(allSpace)
            else:
                l[j].append(rightVertical)
    elif n[i]=='8':
        for j in range(2*s+3):
            if j==0 or j==s+1 or j==2*s+2:
                l[j].append(horizon)
            else:
                l[j].append(halfVertical)
    elif n[i]=='9':
        for j in range(2*s+3):
            if j==0 or j==s+1 or j==2*s+2:
                l[j].append(horizon)
            elif j<s+1:
                l[j].append(halfVertical)
            else:
                l[j].append(rightVertical)
    elif n[i]=='0':
        for j in range(2*s+3):
            if j==0 or j==2*s+2:
                l[j].append(horizon)
            elif j==s+1:
                l[j].append(allSpace)
            else:
                l[j].append(halfVertical)

    for j in range(2*s+3):
        l[j].append(' ')

for i in range(len(l)):
    for j in range(len(l[0])):
        print(l[i][j],end='')
    print()
