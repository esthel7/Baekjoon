from collections import deque

def count(q1,q2,t1,t2,l1,l2,half,cnt,maximum):
    q=[[q1,q2,t1,t2,l1,l2,cnt]]
    while True:
        [q1,q2,t1,t2,l1,l2,cnt]=q.pop()
        if cnt>maximum:
            return -1
        if t1==half:
            return cnt
        if l1==1 and t1>half:
            return -1
        if l2==1 and t2>half:
            return -1
        
        f1=q1[0]
        f2=q2[0]
        if t1>t2:
            q1.popleft()
            q2.append(f1)
            q.append([q1,q2,t1-f1,t2+f1,l1-1,l2+1,cnt+1])
        else:
            q1.append(f2)
            q2.popleft()
            q.append([q1,q2,t1+f2,t2-f2,l1+1,l2-1,cnt+1])
        

def solution(queue1, queue2):
    queue1=deque(queue1)
    queue2=deque(queue2)
    len1=0
    len2=0
    total1=0
    total2=0

    for i in range(len(queue1)):
        len1+=1
        len2+=1
        total1+=queue1[i]
        total2+=queue2[i]
    half=(total1+total2)//2
    if (total1+total2)%2!=0:
        return -1

    return count(queue1,queue2,total1,total2,len1,len2,half,0,3*len1)
