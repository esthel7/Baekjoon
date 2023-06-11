def solution(s):
    answer = -1
    s=list(s)
    s=s+s
    n=len(s)//2
    l=[]
    sMax=0
    for i in range(n):
        flag=0
        for j in range(i,i+n,1):
            if s[j]=='(' or s[j]=='[' or s[j]=='{':
                l.append(s[j])
            elif s[j]==')' or s[j]==']' or s[j]=='}':
                if len(l)==0:
                    flag=1
                    break
                if l[-1]=='(' and s[j]==')' or l[-1]=='[' and s[j]==']' or l[-1]=='{' and s[j]=='}':
                    l.pop(-1)
                    if len(l)==0:
                        sMax+=1
                else:
                    flag=1
                    break
        if flag==1:
            sMax=0
            continue
        else:
            answer=sMax
            break
    if flag==1:
        answer=0
    return answer