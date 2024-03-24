import sys
input=sys.stdin.readline

def find(N,start,answer):
  if start==N:
    now=0
    prev=l[0]
    flag='+'
    final=[str(l[0])]
    for i in range(1,N):
      final.append(answer[i-1])
      final.append(str(l[i]))
      if answer[i-1]==' ':
        prev=prev*10+l[i]
        continue

      if prev!=0:
        if flag=='+':
          now+=prev
        else:
          now-=prev
      prev=l[i]

      if answer[i-1]=='+':
        flag='+'
      else:
        flag='-'

    if flag=='+':
      now+=prev
    elif flag=='-':
      now-=prev
    else:
      return

    if now==0:
      print(''.join(final))
    return

  find(N,start+1,list(answer)+[' '])
  find(N,start+1,list(answer)+['+'])
  find(N,start+1,list(answer)+['-'])

t=int(input())
for _ in range(t):
  N=int(input())
  l=[i for i in range(1,N+1)]
  find(N,1,[])
  print()
