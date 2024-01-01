from bisect import bisect_left

def make(language,career,long,food):
    now=0
    if language=='cpp':
        now+=0
    elif language=='java':
        now+=8
    else:
        now+=16
    
    if career=='backend':
        now+=0
    else:
        now+=4
    
    if long=='junior':
        now+=0
    else:
        now+=2
    
    if food=='chicken':
        now+=0
    else:
        now+=1
    
    return now

def find(l,query,idx):
    q=[]
    q.append([0,idx])
    save=0
    while len(q):
        [now,idx]=q.pop()
        if idx==4:
            # bisect로 시간 조절
            # bisect_left로 가능한 위치 중 가장 왼쪽에 넣기 / bisect_right는 가능한 위치 중 가장 오른쪽에 넣기
            here=bisect_left(l[now],query[idx])
            save+=len(l[now])-here
        elif idx==0:
            if query[idx]=='cpp':
                q.append([now,idx+1])
            elif query[idx]=='java':
                q.append([now+8,idx+1])
            elif query[idx]=='python':
                q.append([now+16,idx+1])
            else:
                q.append([now,idx+1])
                q.append([now+8,idx+1])
                q.append([now+16,idx+1])
        elif idx==1:
            if query[idx]=='backend':
                q.append([now,idx+1])
            elif query[idx]=='frontend':
                q.append([now+4,idx+1])
            else:
                q.append([now,idx+1])
                q.append([now+4,idx+1])
        elif idx==2:
            if query[idx]=='junior':
                q.append([now,idx+1])
            elif query[idx]=='senior':
                q.append([now+2,idx+1])
            else:
                q.append([now,idx+1])
                q.append([now+2,idx+1])
        else: # idx=3
            if query[idx]=='chicken':
                q.append([now,idx+1])
            elif query[idx]=='pizza':
                q.append([now+1,idx+1])
            else:
                q.append([now,idx+1])
                q.append([now+1,idx+1])
    
    return save
                

def solution(info, query):
    answer = []
    l=[[] for i in range(3*2*2*2)]
    
    for i in range(len(info)):
        [language,career,long,food,point]=info[i].split(' ')
        now=make(language,career,long,food)
        l[now].append(int(point))
        
    for i in range(24):
        if len(l[i]):
            l[i].sort()

    for i in range(len(query)):
        [language,career,long,datas]=query[i].split(' and ')
        [food,point]=datas.split(' ')
        answer.append(find(l,[language,career,long,food,int(point)],0))
        
    return answer