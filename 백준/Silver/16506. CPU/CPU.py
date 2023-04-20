import sys
input=sys.stdin.readline

def change(word):
    if word=='0':
        word='000'
    elif word=='1':
        word='001'
    elif word=='2':
        word='010'
    elif word=='3':
        word='011'
    elif word=='4':
        word='100'
    elif word=='5':
        word='101'
    elif word=='6':
        word='110'
    elif word=='7':
        word='111'
    return word

def changeB(word):
    if word=='0':
        word='0000'
    elif word=='1':
        word='0001'
    elif word=='2':
        word='0010'
    elif word=='3':
        word='0011'
    elif word=='4':
        word='0100'
    elif word=='5':
        word='0101'
    elif word=='6':
        word='0110'
    elif word=='7':
        word='0111'
    elif word=='8':
        word='1000'
    elif word=='9':
        word='1001'
    elif word=='10':
        word='1010'
    elif word=='11':
        word='1011'
    elif word=='12':
        word='1100'
    elif word=='13':
        word='1101'
    elif word=='14':
        word='1110'
    elif word=='15':
        word='1111'
    return word

N=int(input())
l=[]
for i in range(N):
    l.append(input().rstrip())

for i in range(N):
    q=[]
    word,d,a,b=l[i].split(' ') # 띄어쓰기 기준으로 나누기

    d=change(d)
    a=change(a)

    if word[-1]=='C':
        word=word[:len(word)-1]
        q4='10'
        b=changeB(b)

    else:
        q4='00'
        b=change(b)
        b=b+'0'
    
    if word=='ADD':
        q.append('0000')
        q.append(q4)
    elif word=='SUB':
        q.append('0001')
        q.append(q4)
    elif word=='MOV':
        q.append('0010')
        q.append(q4)
        a='000'
    elif word=='AND':
        q.append('0011')
        q.append(q4)
    elif word=='OR':
        q.append('0100')
        q.append(q4)
    elif word=='NOT':
        q.append('0101')
        q.append(q4)
        a='000'
    elif word=='MULT':
        q.append('0110')
        q.append(q4)
    elif word=='LSFTL':
        q.append('0111')
        q.append(q4)
    elif word=='LSFTR':
        q.append('1000')
        q.append(q4)
    elif word=='ASFTR':
        q.append('1001')
        q.append(q4)
    elif word=='RL':
        q.append('1010')
        q.append(q4)
    else:
        q.append('1011')
        q.append(q4)
    
    q.append(d)
    q.append(a)
    q.append(b)

    for i in range(len(q)):
        print(q[i],end='')
    print()
