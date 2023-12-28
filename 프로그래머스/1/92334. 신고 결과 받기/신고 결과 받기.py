def solution(id_list, report, k):
    n=len(id_list)
    answer=[0 for i in range(n)]
    names=[[]for i in range(n)] # 고발한 사람들
    name={}
    for i in range(n):
        name[id_list[i]]=i
    
    for i in range(len(report)):
        [do,sad]=report[i].split(' ')
        if do not in names[name[sad]]:
            names[name[sad]].append(do)

    for i in range(n):
        nameLen=len(names[i])
        if nameLen>=k:
            for j in range(nameLen):
                person=names[i][j]
                answer[name[person]]+=1

    return answer
