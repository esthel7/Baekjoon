def solution(id_list, report, k):
    person=len(id_list)
    num=len(report)

    info={} # 신고한 사람들 저장
    name={} # 해당 name idx 저장
    for i in range(person):
        info[id_list[i]]=[]
        name[id_list[i]]=i

    for i in range(num):
        do,sad=report[i].split(' ')
        if do in info[sad]:
            continue
        info[sad].append(do)
        
    answer = [0 for i in range(person)]
    for i in range(person):
        if len(info[id_list[i]])>=k:
            for item in info[id_list[i]]:
                answer[name[item]]+=1
    
    return answer