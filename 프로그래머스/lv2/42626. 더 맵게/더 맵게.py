import heapq

def solution(scoville, K):
    answer = 0
    n=len(scoville)
    heap=[]
    for i in range(n):
        heapq.heappush(heap,scoville[i])
    # scoville=sorted(scoville)
    # if scoville[0]>=K:
    if heap[0]>=K:
        return 0
    cnt=0
    while 1<n:
        # new=scoville.pop(0)+scoville.pop(0)*2
        new=heapq.heappop(heap)+heapq.heappop(heap)*2
        # scoville.append(new)
        heapq.heappush(heap,new)
        cnt+=1
        # scoville=sorted(scoville)
        # if scoville[0]>=K:
        if heap[0]>=K:
            return cnt
        n-=1
    answer=-1
    return answer