import sys
import heapq
input=sys.stdin.readline

# 0아니면 배열에 추가
# 0이면 절댓값 제일 작은 값 출력 후 배열에서 제거

N=int(input())
q=[]
mq=[]
for i in range(N):
    a=int(input())
    if a!=0:
        if a>0:
            heapq.heappush(q,a)
        else:
            heapq.heappush(mq,-a)
    else:
        if len(q)==0 and len(mq)==0:
            print(0)
        elif len(q)==0:
            print(-1*heapq.heappop(mq))
        elif len(mq)==0:
            print(heapq.heappop(q))
        elif q[0]>=mq[0]:
            print(-1*heapq.heappop(mq))
        else:
            print(heapq.heappop(q))
