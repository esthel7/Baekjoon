n=int(input())
l=list(map(int,input().split()))

s=[]
answer=[]
for i in range(n):
  while True:
    if len(s)==0:
      answer.append(0)
      s.append([l[i],i+1])
      break
    else:
      if s[-1][0]<l[i]:
        s.pop()
      else:
        answer.append(s[-1][1])
        s.append([l[i],i+1])
        break

for i in range(n):
  print(answer[i],end=' ')
