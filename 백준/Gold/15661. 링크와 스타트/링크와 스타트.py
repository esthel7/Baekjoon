import sys
input=sys.stdin.readline
n=int(input())
score=[list(map(int,input().split(" "))) for _ in range(n)]
answer=10**9
for i in range(1,2**(n-1)):
    leejinsu=format(i,'b').zfill(n)
    start,link=[],[]#0은 스타트 1은 링크
    start_score,link_score=0,0
    for i in enumerate(leejinsu):
        if i[1]=="0":
            start.append(i[0])
        else:
            link.append(i[0])
    if len(start)>=2:
        for j in range(len(start)):
            for k in range(j+1,len(start)):
                start_score+=score[start[j]][start[k]]+score[start[k]][start[j]]
    if len(link)>=2:
        for j in range(len(link)):
            for k in range(j+1,len(link)):
                link_score+=score[link[j]][link[k]]+score[link[k]][link[j]]
    answer=min(answer,abs(start_score-link_score))
print(answer)