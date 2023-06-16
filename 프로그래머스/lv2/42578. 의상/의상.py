def solution(clothes):
    
    def cal(start,C,now):
        for i in range(start,C):
            now*=length[i]
            add.append(now)
            cal(i+1,C,now)
            now//=length[i]

    answer = 0
    clo={}
    groups=[]
    n=len(clothes)
    for i in range(n):
        wear,group=clothes[i][0],clothes[i][1]
        if group in clo:
            clo[group].append(wear)
        else:
            clo[group]=[wear]
            groups.append(group) # key
    
    C=len(clo)
    length=[0 for i in range(C)]
    answer=1
    for i in range(C):
        length[i]=len(clo[groups[i]])
        answer*=length[i]+1

#     add=[]
#     cal(0,C,1)

#     for j in range(len(add)):
#         answer+=add[j]
                
    return answer-1