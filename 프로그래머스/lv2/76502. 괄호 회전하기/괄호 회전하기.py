def run(s):
    start=['(','{','[']
    l=[]
    for i in range(len(s)):
        if s[i] in start:
            l.append(s[i])
        else:
            if len(l)>0:
                if s[i]==')' and l[-1]=='(' or s[i]==']' and l[-1]=='[' or s[i]=='}' and l[-1]=='{':
                    l.pop(-1)
                    continue
                else:
                    return 0
            else:
                return 0
    if len(l)>0:
         return 0
    return 1

def solution(s):
    num=0
    s=list(s)
    for i in range(len(s)):
        num+=run(s)
        a=s.pop(0)
        s.append(a)
    return num