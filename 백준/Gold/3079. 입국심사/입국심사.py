import sys
input=sys.stdin.readline

N,M=map(int,input().split())
l=[]
for i in range(N):
  l.append(int(input()))

start=min(l)
end=max(l)*M
answer=end
while start<=end:
  mid=(start+end)//2
  cnt=0
  for i in range(N):
    cnt+=mid//l[i]

  if cnt>=M:
    if answer>mid:
      answer=mid
    end=mid-1
  else:
    start=mid+1

print(answer)
