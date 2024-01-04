def find(p,play,adv):
    prev=0
    for i in range(adv):
        prev+=p[i]
    total[0][0]=prev # how long
    total[0][1]=0 # clock
    
    start=1
    end=start+adv-1
    while end!=play:
        now=prev
        now-=p[start-1]
        now+=p[end]
        if now>total[0][0]:
            total[0][0]=now
            total[0][1]=start
        prev=now
        start+=1
        end+=1
            

total=[[0,0]]

def solution(play_time, adv_time, logs):
    answer = ''
    
    [h,m,s]=play_time.split(':')
    play=int(s)+int(m)*60+int(h)*60*60
    p=[0 for i in range(play)]
    
    [h,m,s]=adv_time.split(':')
    adv=int(s)+int(m)*60+int(h)*60*60
    
    for i in range(len(logs)):
        [start,end]=logs[i].split('-')
        
        [h,m,s]=start.split(':')
        start=int(s)+int(m)*60+int(h)*60*60
        
        [h,m,s]=end.split(':')
        end=int(s)+int(m)*60+int(h)*60*60
        
        p[start]+=1
        if end<play:
            p[end]-=1
    
    for i in range(1,play):
        p[i]+=p[i-1]

    find(p,play,adv)
    h=total[0][1]//3600
    total[0][1]%=3600
    m=total[0][1]//60
    total[0][1]%=60
    s=total[0][1]
    
    if h<10:
        h='0'+str(h)
    if m<10:
        m='0'+str(m)
    if s<10:
        s='0'+str(s)
    
    answer=str(h)+':'+str(m)+':'+str(s)
    
    return answer