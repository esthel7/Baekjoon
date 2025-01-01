import sys
input=sys.stdin.readline

def change(now):
  value=0
  i=0
  while i<len(now):
    if i+1<len(now):
      check=now[i]+now[i+1]
      if check in info:
        value+=info[check]
        i+=2
        continue
    value+=info[now[i]]
    i+=1
  return value


first=list(input().rstrip())
second=list(input().rstrip())

info={}
info['MMM']=3000
info['MM']=2000
info['M']=1000
info['CM']=900
info['D']=500
info['CD']=400
info['CCC']=300
info['CC']=200
info['C']=100
info['XC']=90
info['L']=50
info['XL']=40
info['XXX']=30
info['XX']=20
info['X']=10
info['IX']=9
info['V']=5
info['IV']=4
info['III']=3
info['II']=2
info['I']=1

total=change(first)
total+=change(second)

print(total)
answer=[]
Key=list(info.keys())
for item in Key:
  if info[item]<=total:
    answer.append(item)
    total-=info[item]
  if total==0:
    break

print(''.join(answer))
