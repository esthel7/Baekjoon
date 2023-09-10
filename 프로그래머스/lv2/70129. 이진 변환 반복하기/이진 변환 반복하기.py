def change(s): # 자릿수
    num=1
    cnt=0
    l=[]
    while s!=0:
        if num>s:
            if len(l)==0:
                l=['0' for i in range(cnt)]
            s=s-num//2
            l[cnt-1]='1'
            cnt=0
            num=1
            continue
        num*=2
        cnt+=1
    return list(reversed(l))

def run(s): # 0 remove
    remove=0
    for i in range(len(s)):
        if s[i]=='0':
            remove+=1
    return [len(s)-remove,remove]

def solution(s):
    num=0
    remove=0
    while s!='1':
        value=run(s)
        num+=1
        remove+=value[1]
        newS=value[0]
        newS=change(newS)
        s=''.join(newS)
    
    return [num,remove]