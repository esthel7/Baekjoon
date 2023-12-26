def check(ty,tm,td,p):
    if ty>p[0]:
        return True
    if ty<p[0]:
        return False
    if ty==p[0]:
        if tm>p[1]:
            return True
        if tm<p[1]:
            return False
        if tm==p[1]:
            if td>=p[2]:
                return True
            if td<p[2]:
                return False
            

def find(ty,tm,td,t,p,T,P):
    answer=[]
    for i in range(P):
        for j in range(T):
            if p[i][3]==t[j][0]:
                remain=t[j][1]
                ry=remain//12
                rm=remain%12
                break
        if p[i][1]+rm>12:
            p[i][0]+=1
            p[i][1]=p[i][1]+rm-12   
        else:
            p[i][1]+=rm
        p[i][0]+=ry
        if check(ty,tm,td,p[i]):
            answer.append(i+1)
    return answer

def solution(today, terms, privacies):
    [y,m,d]=today.split('.')
    ty=int(y)
    tm=int(m)
    td=int(d)
    
    t=[]
    T=len(terms)
    for i in range(T):
        [name,L]=terms[i].split(' ')
        t.append([name,int(L)])
        
    p=[]
    P=len(privacies)
    for i in range(P):
        [dates,term]=privacies[i].split(' ')
        [y,m,d]=dates.split('.')
        y=int(y)
        m=int(m)
        d=int(d)
        p.append([y,m,d,term])
    
    return find(ty,tm,td,t,p,T,P)