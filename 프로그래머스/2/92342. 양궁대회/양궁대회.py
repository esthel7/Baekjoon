def compare(diff,minset,now):
    if diff<=0 or minset[0]==11:
        return
    if len(save):
        if calculate[0]<diff:
            calculate[0]=diff
            save[0]=now
            minbox[0][0]=minset[0]
            minbox[0][1]=minset[1]
        elif calculate[0]==diff:
            if minbox[0][0]>minset[0]:
                save[0]=now
                minbox[0][0]=minset[0]
                minbox[0][1]=minset[1]
            elif minbox[0][0]==minset[0]:
                if minbox[0][1]<minset[1]:
                    save[0]=now
                    minbox[0][1]=minset[1]
    else:
        calculate.append(diff)
        save.append(now)
        minbox.append(minset)

def find(n,info):
    apoint=0
    for i in range(11):
        if info[i]:
            apoint+=10-i
    
    q=[[0,0,apoint,0,[0 for i in range(11)],11,0]]
    
    while len(q):
        [idx,lpoint,apoint,cnt,now,minnum,mincount]=q.pop()
        # 현재과녁, lian, apeach, 화살수, 현재배열, 가장적은point, 가장적은point횟수
        if cnt==n:
            compare(lpoint-apoint,[minnum,mincount],now)
            continue
        if idx>10:
            now=list(now)
            now[10]+=n-cnt
            compare(lpoint-apoint,[0,now[10]],now)
            continue

        q.append([idx+1,lpoint,apoint,cnt,now,minnum,mincount])
            
        if info[idx]+1+cnt<=n:
            minnum=10-idx
            mincount=info[idx]+1
            now=list(now)
            now[idx]=mincount
            if info[idx]:
                q.append([idx+1,lpoint+minnum,apoint-minnum,cnt+mincount,now,minnum,mincount])
            else:
                q.append([idx+1,lpoint+minnum,apoint,cnt+mincount,now,minnum,mincount])
    

calculate=[] # 점수차이
save=[] # 화살점수표
minbox=[] # [최솟값,횟수]
def solution(n, info):
    find(n,info)
    if len(save):
        return save[0]
    return [-1]