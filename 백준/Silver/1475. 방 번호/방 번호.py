N=list(input())
cnt=1
flag=7
now=[7 for i in range(10)]
for i in range(len(N)):
  num=int(N[i])-1
  if num==5 or num==8:
    if now[5]>=flag:
      now[5]-=1
      continue
    elif now[8]>=flag:
      now[8]-=1
      continue
    else:
      cnt+=1
      flag-=1
      now[num]-=1
  else:
    if now[num]>=flag:
      now[num]-=1
      continue
    else:
      cnt+=1
      flag-=1
      now[num]-=1
print(cnt)
