def find(N,S,start,num,total):
  if total==S and num:
    cnt[0]+=1
  for i in range(start,N):
    num.append(i)
    find(N,S,i+1,num,total+l[i])
    num.pop()

N,S=map(int,input().split())
l=list(map(int,input().split()))
cnt=[0]

find(N,S,0,[],0)

print(cnt[0])
