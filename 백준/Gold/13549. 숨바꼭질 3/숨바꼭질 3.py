import sys
input=sys.stdin.readline

def find():
    final=100000
    q=[]
    q.append([N,0])
    while len(q)>0:
        now,count=q.pop(0)
        if final+2<=count:
            break
        if now==K:
            if final>count:
                final=count
            continue
        if now*2<=200000 and visited[now*2]>=count+1:
            visited[now*2]=count+1
            q.append([now*2,count])
        if now-1>=0 and visited[now-1]>=count+1:
            visited[now-1]=count+1
            q.append([now-1,count+1])
        if now+1<=100000 and visited[now+1]>=count+1:
            visited[now+1]=count+1
            q.append([now+1,count+1])
    
    print(final)

N,K=map(int,input().split())

visited=[100000 for i in range(200001)]
visited[N]=0
find()
