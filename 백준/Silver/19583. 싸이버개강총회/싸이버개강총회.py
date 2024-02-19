import sys
input=sys.stdin.readline

# 00:00 ~ Q
# S+ ~ E- 인정 x

def change(input):
  hour,minute=input.split(':')
  return [hour,minute]

S,E,Q=input().rstrip().split(' ')
S=change(S)
E=change(E)
Q=change(Q)

person={}
while True:
  now=input().rstrip()
  if now=='':
    break
  time,name=now.split(' ')
  time=change(time)
  if time[0]>Q[0] or (time[0]==Q[0] and time[1]>Q[1]):
    continue
  if time[0]<S[0] or (time[0]==S[0] and time[1]<=S[1]):
    person[name]=False
  elif time[0]>E[0] or (time[0]==E[0] and time[1]>=E[1]):
    if name in person.keys():
      person[name]=True

answer=0
for name in person:
  if person[name]:
    answer+=1
print(answer)
