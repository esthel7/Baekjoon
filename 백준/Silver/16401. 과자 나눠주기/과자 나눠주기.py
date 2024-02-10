M,N=map(int,input().split())
l=list(map(int,input().split()))
l.sort(reverse=True)

if N>M:
  N=M

start=1
end=l[0]
answer=0
while start<=end:
  mid=(start+end)//2
  now=0
  for i in range(N):
    now+=l[i]//mid
  if now>=M:
    answer=mid
    start=mid+1
  else:
    end=mid-1
    # if answer!=0:
    #   break

print(answer)
