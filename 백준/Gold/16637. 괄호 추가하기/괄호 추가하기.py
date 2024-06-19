import sys
input=sys.stdin.readline

def cal(b,c,d):
  if c=='*':
    return [b*d]
  elif c=='+':
    return [b+d]
  else: # -
    return [b-d]


def make(a,b,c,d):
  b=int(b)
  d=int(d)
  value=cal(b,c,d)
  return [a]+value

def find(idx,now):
  global answer
  if idx==Half:
    if answer=='first':
      answer=now
    elif answer<now:
      answer=now
    return answer
  if dp[0][idx][0]=='*':
    find(idx+1,now*dp[0][idx][1])
  elif dp[0][idx][0]=='+':
    find(idx+1,now+dp[0][idx][1])
  else: # -
    find(idx+1,now-dp[0][idx][1])
  
  if idx+2<=Half:
    if dp[1][idx][0]=='*':
      find(idx+2,now*dp[1][idx][1])
    elif dp[1][idx][0]=='+':
      find(idx+2,now+dp[1][idx][1])
    else: # -
      find(idx+2,now-dp[1][idx][1])


N=int(input())
N+=1
Half=N//2
l=['+']+list(input().rstrip())

dp=[['' for i in range(Half)]for j in range(2)]

for i in range(Half):
  dp[0][i]=[l[i*2],int(l[i*2+1])]
  if i!=Half-1:
    dp[1][i]=make(l[i*2],l[i*2+1],l[i*2+2],l[i*2+3])

answer='first'
find(0,0)
print(answer)
