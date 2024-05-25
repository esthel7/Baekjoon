import sys
input=sys.stdin.readline

def find(value):
  cnt=0
  for i in range(K):
    cnt+=l[i]//value

  if cnt>=N:
    possible.append(value)
    return True
  else: # 줄이기
    return False


K,N=map(int,input().split())
l=[]
for i in range(K):
  l.append(int(input()))

possible=[]
start=1
end=sum(l)//N
while start<=end:
  mid=(start+end)//2
  if mid==0:
    break
  if find(mid):
    start=mid+1
  else:
    end=mid-1

print(max(possible))
