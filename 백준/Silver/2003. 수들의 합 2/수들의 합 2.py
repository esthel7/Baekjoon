import sys
input=sys.stdin.readline

N,M=map(int,input().split())
l=list(map(int,input().split()))

start=0
end=0
now=l[start]
answer=0
while True:
  if now==M:
    answer+=1
    now-=l[start]
    start+=1
    end+=1
    if end==N:
      break
    now+=l[end]
  elif now<M:
    end+=1
    if end==N:
      break
    now+=l[end]
  else:
    now-=l[start]
    start+=1

print(answer)
