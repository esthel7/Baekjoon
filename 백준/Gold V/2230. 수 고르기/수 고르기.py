import sys
input=sys.stdin.readline

# n개 정수 수열, 차이가 M이상이면서 가장 작은 경우

N,M=map(int,input().split())
l=[]
for i in range(N):
  l.append(int(input()))

l.sort()

start=0
end=1
answer=-1
while end<N:
  diff=l[end]-l[start]
  if diff==M:
    answer=M
    break
  elif diff<M:
    if end+1==N:
      break
    end+=1
  else:
    if answer==-1 or answer>diff:
      answer=diff
    start+=1
    if start==end:
      if end+1<N:
        end+=1
      else:
        break

print(answer)
