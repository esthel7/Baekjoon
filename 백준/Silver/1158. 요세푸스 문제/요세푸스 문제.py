N,K=map(int,input().split())

l=[i for i in range(1,N+1)]
answer=[]
now=K-1
cnt=N
while True:
  answer.append(l.pop(now))

  cnt-=1
  now+=K-1
  if cnt==0:
    break
  now%=cnt

print('<',end='')
for i in range(N-1):
  print('%d, '%answer[i],end='')
print('%d>'%(answer[N-1]))
