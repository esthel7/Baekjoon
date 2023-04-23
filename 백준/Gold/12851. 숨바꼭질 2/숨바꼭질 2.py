import sys
input=sys.stdin.readline

def find():
    global final,lastCount
    q=[]
    q.append([N,0])
    while len(q)>0:
        now,count=q.pop(0)
        if final<count:
            break
        if now==K:
            if final>count:
                final=count
                lastCount=1
            elif final==count:
                lastCount+=1
            continue
        if now-1>=0:
            if visited[now-1]>=count+1 or now-1==K:
                visited[now-1]=count+1
                q.append([now-1,count+1])
        if now+1<=100000:
            if visited[now+1]>=count+1 or now+1==K:
                visited[now+1]=count+1
                q.append([now+1,count+1])
        if now*2<=200000:
            if visited[now*2]>=count+1 or now*2==K:
                visited[now*2]=count+1
                q.append([now*2,count+1])
    
    print(final)
    print(lastCount)


N,K=map(int,input().split())

visited=[100000 for i in range(200001)]
visited[N]=1
final=100000
lastCount=0
find()
