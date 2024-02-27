from collections import deque

# 맨앞 pop, 뒤로 insert

def solution(queue1, queue2):
    t1=sum(queue1)
    t2=sum(queue2)
    n=len(queue1)*3

    if (t1+t2)%2==1:
        return -1
    
    goal=(t1+t2)//2
    
    queue1=deque(queue1)
    queue2=deque(queue2)
    
    q=deque([[t1,t2,queue1,queue2,0]])
    
    while q:
        t1,t2,q1,q2,cnt=q.popleft()
        if cnt>n:
            answer=-1
            break

        if t1==goal:
            answer=cnt
            break

        if t1>t2:
            left=q1.popleft()
            if left>goal:
                answer=-1
                break
            q2.append(left)
            q.append([t1-left,t2+left,q1,q2,cnt+1])
        else:
            left=q2.popleft()
            if left>goal:
                answer=-1
                break
            q1.append(left)
            q.append([t1+left,t2-left,q1,q2,cnt+1])
    
    return answer