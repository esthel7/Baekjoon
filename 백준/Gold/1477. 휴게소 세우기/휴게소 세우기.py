import sys
import heapq
input=sys.stdin.readline

N,M,L=map(int,input().split())
l=list(map(int,input().split()))
l.sort()

if N==0:
  if L%(M+1)==0:
    print(L//(M+1))
  else:
    print(L//(M+1)+1)
  exit(0)

diff=[0 for i in range(N+1)]
diff[0]=l[0]
q=[]
heapq.heappush(q,[-l[0],0])
for i in range(1,N):
  heapq.heappush(q,[-(l[i]-l[i-1]),i])
  diff[i]=l[i]-l[i-1]
heapq.heappush(q,[-(L-l[N-1]),N])
diff[N]=L-l[N-1]

cnt=[1 for i in range(N+1)]
for i in range(M):
  dis,idx=heapq.heappop(q)
  cnt[idx]+=1
  if diff[idx]%cnt[idx]==0:
    heapq.heappush(q,[-(diff[idx]//cnt[idx]),idx])
  else:
    heapq.heappush(q,[-(diff[idx]//cnt[idx])-1,idx])

answer,idx=heapq.heappop(q)
print(-answer)
